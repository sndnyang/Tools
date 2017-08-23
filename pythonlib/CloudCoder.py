# -*- coding: utf-8 -*-
import os
import re

from evernote.api.client import EvernoteClient
from evernote.edam.notestore import NoteStore

def replace_html(s):
    s = s.replace('&quot;','"')
    s = s.replace('&amp;','&')
    s = s.replace('&lt;','<')
    s = s.replace('&gt;','>')
    s = s.replace('&nbsp;',' ')
    s = s.replace('\xc2\xa0','')
    return s

class CloudCoder:

    def __init__(self):
        self.auth_token = "os.environ.get('EVERNOTE_TOKEN', None)"

    def get_client(self):
        sandbox = False
        china = True
        self.client = EvernoteClient(token=self.auth_token, sandbox=sandbox, china=china)
        self.note_store = self.client.get_note_store()

    def filterNotes(self, filter, num):
        spec = NoteStore.NotesMetadataResultSpec()
        spec.includeTitle = True
        self.get_client()
        ourNoteList = self.note_store.findNotesMetadata(self.auth_token, filter, 0, num, spec)
        return ourNoteList

    def get_markdown(self, match):
        if self.auth_token:
            # Set up the NoteStore client
            filter = NoteStore.NoteFilter()
            filter.words = "notebook:我的第一个笔记本 " + match

            ourNoteList = self.filterNotes(filter, 1)
            if not ourNoteList.notes:
                return "Error: not find note"
            note = ourNoteList.notes[0]
            self.note = self.note_store.getNote(self.auth_token, note.guid, True, False, False, False)
            code = re.sub("<.*?>", '', self.note.content.replace("</d", "\n</d"))
            return replace_html(code)

        return "Error: no token"

    def get_json(self, match):
        return self.convert_md_json(self.get_markdown(match))

    def convert_md_json(self, content):
        if content.startswith("Error: "):
            return content
        maps = {}
        lines = content.replace("\r", "").split("\n")
        self.to_hierarchy_json(maps, lines, 0, 0)
        return maps

    def to_hierarchy_json(self, maps, lines, level, lineno):
        if len(lines) == lineno:
            return 0, lineno
        l = lines[lineno]

        name = "code"
        
        if not l.strip():
            return self.to_hierarchy_json(maps, lines, level, lineno+1)
        # print '%4d %4d' % (level, lineno),
        
        while l.startswith("#"):
            sharp_count = len(l.split(" ", 1)[0])
            name = l.split(" ", 1)[1]
            # print '%4s %4s' % (name, sharp_count)
            # print l
            if level >= sharp_count:
                return sharp_count, lineno
            elif level < sharp_count:
                maps[name] = {"code": ""}
                tmp, lineno = self.to_hierarchy_json(maps[name], lines, level+1, lineno+1)
                if tmp < level or not tmp:
                    return tmp, lineno
                l = lines[lineno]       
        # print "add to ", name
        if name == "code":
            maps[name] += l + '\n'
        else:
            maps[name]["code"] += l + '\n'    
        # print l
        return self.to_hierarchy_json(maps, lines, level, lineno+1)

    def get_code(self, match, keys="all"):
        return self.get_code_by_parts(match, keys)

    def get_code_by_parts(self, match, keys):
        json = self.get_json(match)
        if isinstance(json, str) and json.startswith("Error: "):
            return json
        return self.filter_json(json, keys)

    def filter_json(self, json, keys):
        if keys == "all":
            return self.convert_json_plain(json, '')
        maps = {'调用':"call", "定义":"implement", "实现":"implement"}
        keys = [e.lower() for e in keys]
        en_maps = [maps[e] for e in keys if e in maps]
        parts = []
        for k in json:
            if k.lower() in keys or k.lower() in en_maps:
                parts.append(self.convert_json_plain(json[k], k))
            elif isinstance(json[k], dict):
                result = self.filter_json(json[k], keys)
                if result:
                    parts.append(result)
        return '\n'.join(parts)

    def convert_json_plain(self, json, key):
        lines = [key]
        for k in json:
            if isinstance(json[k], dict):
                lines.append(self.convert_json_plain(json[k], k))
            elif isinstance(json[k], str):
                if k != "code":
                    lines.append(k)
                lines.append(json[k])
        return '\n'.join(lines)
