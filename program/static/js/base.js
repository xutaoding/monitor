$(function(){
    $('[data-toggle="modal"]').click(function(){
        var data_id = $(this).attr('data-id');
        alert($('[data-id="' + data_id +'"]').html());
    });



});