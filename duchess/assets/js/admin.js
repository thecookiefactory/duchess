$(function(){

    $('#add-slide').submit(function(event){
        event.preventDefault();
        var row = $(this).find('tr');
        var data = {
            'id': row.find('input.slide-id').val(),
            'text': row.find('input.slide-text').val(),
            'image': row.find('input.slide-image').val()
        };
        $.post('/api/slides', data, function(response){
            var last_data_row = $('#add-slide').parents('tr').prev();
            last_data_row.after(last_data_row[0].outerHTML);
            var last_data_row = $('#add-slide').parents('tr').prev();
            last_data_row.find('td.slide-id').text(data['id']);
            last_data_row.find('td.slide-text').text(data['text']);
            last_data_row.find('td.slide-image a').text(data['image']);
            row.find('input.slide-id').val(response.random_id);
            row.find('input.slide-text').val('');
            row.find('input.slide-image').val('');
            row.find('input.slide-text').focus();
        });
    });
});
