$(function(){
    $('[data-toggle="modal"]').click(function(){
        var records = [];
        var data_id = $(this).attr('data-id');
        console.log(data_id );
        console.log('[data-id="' + data_id + '"] td');

        $('[data-id="' + data_id + '"] td').each(function(i){
            var value = $(this).attr('class');

            if (value != "extra"){
                records.push($(this).text());
                console.log($(this).text());
            }
        });

//        alert(records);
    });



});