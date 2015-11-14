var objects_modal = null;

$(function(){
    $('[data-toggle="modal"]').click(function(){
        objects_modal = null;
        objects_modal = {};

        var data_id = $(this).attr('data-id');
            selector = $(this).attr('data-target');

        if (selector == '#update'){
            var keys = ['id', 'secu', 'y', 'price', 'volu', 'amou', 'disc', 'ratio', 'buy', 'sale', 'c.en', 'crt'];

            $('[data-id="' + data_id + '"] td').each(function(index){
                if($(this).attr('class') != 'extra'){
                    if (index == 0){
                        objects_modal[keys[index]] = data_id;
                    } else{
                        objects_modal[keys[index]] = $(this).text().trim();
                    }
                }
            });
            console.log(objects_modal);
            $(".data-id").val(objects_modal['id']);
        }

    });

    $("div.update ul li").click(function(){
        var key = $(this).attr('class'),
            maps = {'secu': '股票代码', 'y': '交易日期', 'price': '成交价', 'volu': '成交量', 'amou': '成交额',
                   'disc': 'disc', 'ratio': 'ratio', 'buy': '买入营业部', 'sale': '卖出营业部', 'c.en': '货币'}

        var html = '<div class="form-group data-check"><label class="col-sm-3 control-label">'
                    + maps[key] +'：</label><div class="col-sm-9"><input type="text" class="form-control input-xs"'
                    + ' name="secu" value="' + objects_modal[key] + '"></div></div>';
        $('form.update').append(html);

        console.log(objects_modal);
    });


});