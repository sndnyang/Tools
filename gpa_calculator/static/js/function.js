/**
 * Created by 80274869 on 2014-9-4.
 */

function calit()
{
    var content = $("#grade").val();
    var type = $("#type").val();
    
    var elements = new Array("课程名", "百分制", "4分制", "等级制", "学分", "学时");

    var map = {'csv':',', 'space':' ', ',':',', ' ':' ', '空格':' ', '逗号':','};

    var lines = content.split(/\r?\n/);

    var table = $('<table border="1"></table>');
    
    var divs = new Array();
    var findex = 0;
    
    var row = $('<tr></tr>');
    for (var i = 0; i < elements.length; i++) 
    {
        var cell = $('<th>' + elements[i] + '</th>');    
        row.append(cell);
    }    
    
    table.append(row);
    
    var optbox = document.getElementsByName("select");
    
    for (i = 0; i < lines.length; i++)
    {
        var line = lines[i];

        if (type != ' ' && type != '空格' && type != 'space')
        {
            line = line.replace(/\s+/g, "");
        }
        else 
        {
            line = line.replace(/\s+/g, " ");
            type = ' ';
        }

        row = $('<tr></tr>');
        
        var fields = line.split(type);
        var c = 0;
        for (var j = 0; j < elements.length; j++) 
        {
            var text;
            if (optbox[j].checked)
            {
                text = fields[c];
                c++;
            } 
            else 
            {
                text = "";
            }
            var cell = $('<td>' + text + '</td>');
            row.append(cell);            
        }
        table.append(row);
    }
   
    $('#content').append(table);
}

function createFieldElement(id, value)
{
    var addiv = document.createElement("input");
    addiv.id = id;
    addiv.type = "text";
    addiv.value = value;

    return addiv;
}
