// Hide save and cancel buttons on load
$(document).find('.btn-save').hide();
$(document).find('.btn-cancel').hide();

// Make data cell editable on click
$(document).on('click', '.row-data', function(event)
{
    event.preventDefault();

    if($(this).attr('edit-type') == 'button')
    {
        return false;
    }

    $(this).closest('div').attr('contenteditable', 'true');
    $(this).focus();
});

// Make table row editable on button click
$(document).on('click', '.btn-edit', function(event)
{
    event.preventDefault();
    var table_row = $(this).closest('tr');
    var row_id = table_row.attr('row-id');

    table_row.find('.btn-save').show();
    table_row.find('.btn-cancel').show();
    table_row.find('.btn-edit').hide();
    table_row.find('.row-data').attr('contenteditable', 'true');
    table_row.find('.row-data').attr('edit-type', 'button');
    table_row.find('.row-data').each(function(index, val)
    {
        $(this).attr('original-entry', $(this).html());
    });
});

// Cancel user table entry
$(document).on('click', '.btn-cancel', function(event)
{
    event.preventDefault();

    var table_row = $(this).closest('tr');
    var row_id = table_row.attr('row-id');

    table_row.find('.btn-save').hide();
    table_row.find('.btn-cancel').hide();
    table_row.find('.btn-edit').show();
    table_row.find('.row-data').attr('edit-type', 'click');
    table_row.find('.row-data').each(function(index,val)
    {
        $(this).html($(this).attr('original-entry'));
    });
});

// Save entire table row entry
$(document).on('click', '.btn-save', function(event)
{
    event.preventDefault();

    var table_row = $(this).closest('tr');
    var row_id = table_row.attr('row-id');
    table_row.find('.btn-save').hide();
    table_row.find('.btn-cancel').hide();
    table_row.find('.btn-edit').show();
    table_row.find('.row-data').attr('edit-type', 'click');

    var arr = {};
    table_row.find('.row-data').each(function(index, val)
    {
        var col_name = $(this).attr('col_name');
        var col_val = $(this).html();
        arr[col_name] = col_val;
    });

    $.ajax({
        type: 'POST',
        contentType: 'application/json',
        url: '/workout',
        dataType: 'json',
        data: JSON.stringify(arr),
    });
});
