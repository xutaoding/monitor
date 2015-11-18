var objects_modal = null;

$(function(){
    $('[data-toggle="modal"]').click(function(){
        objects_modal = null;

        var data_id = $(this).attr('data-id'),
            selector = $(this).attr('data-target');
        objects_modal = {'id': data_id}
        console.log(objects_modal);

        var keys = ['no', 'secu', 'y', 'price', 'volu', 'amou', 'disc', 'ratio', 'buy', 'sale', 'c.en', 'crt'];

        $('[data-id="' + data_id + '"] td').each(function(index){
            if($(this).attr('class') != 'extra'){
                objects_modal[keys[index]] = $(this).text().trim();
            }
        });
        console.log(objects_modal);
        $(".data-id").val(objects_modal['id']);

        if(selector == '#delete'){
            var html = '',
            maps = {'no': '序号', 'secu': '股票代码', 'y': '交易日期'};

            for (attr in maps){
                html += '<div class="form-group data-show"><label class="col-sm-3 control-label">' + maps[attr] + ': </label>' +
                    '<div class="col-sm-8"><input class="form-control input-xs" type="text" value="' +
                    objects_modal[attr] + '" disabled></div></div>';
            }
            $(selector + ' .modal-body .data-show').remove();
            $('.fix-control').before(html);
        }

    });

    $("div.update ul li").click(function(){
        var key = $(this).attr('class'),
            maps = {'secu': '股票代码', 'y': '交易日期', 'price': '成交价', 'volu': '成交量', 'amou': '成交额',
                   'disc': 'disc', 'ratio': 'ratio', 'buy': '买入营业部', 'sale': '卖出营业部', 'c.en': '货币'}

        var minus = '<button type="button" class="btn btn-danger btn-xs remove" style="margin-top: 6px">' +
                    '<span class="glyphicon glyphicon-minus"></span></button>'
        var html = '<div class="form-group data-check"><label class="col-sm-3 control-label">'
                    + maps[key] +'：</label><div class="col-sm-8"><input type="text" class="form-control input-xs"'
                    + ' name="' + key + '" value="' + objects_modal[key] + '"></div>' + minus + '</div>';
        $('.update-submit').before(html);
    });

    $(document).on('click', '.remove', function(){
        $(this).parent('.data-check').remove();
    })

    $('.ensure-delete').click(function(){
        var csrftoken = $.cookie('csrftoken');
        function csrfSafeMethod(method) {
            // these HTTP methods do not require CSRF protection
            return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
        }

        $.ajaxSetup({
            beforeSend: function(xhr, settings) {
                if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                    xhr.setRequestHeader("X-CSRFToken", csrftoken);
                }
            }
        });

        console.log($(this).siblings('input.data-id').attr('value'));
        $.ajax({
            url: "/program/block_trade/",
            data: {'id': $(this).siblings('input.data-id').attr('value')},
            type: "DELETE",
            success: function(data){
                var obj = JSON.parse(data);
                $('#delete').modal('hide');

                if (!obj.success){
                    alert(obj.msg);
                }

                window.location.reload(); // Refresh the current web page
                // window.location.href = '/..../' // Jump to the specified page
            }
        });
    });

});
