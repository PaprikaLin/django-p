// $(document).ready(function() {
//     $('.post-title a').click(function(event){
//         event.preventDefault();
//         $('#ajaxbody').load(this.href)
//     })
// });


$('.text img').each(function(imgIndex){
    $(this).css('max-width', '100%');
    $(this).css('max-height', '500px').click(function() {
        var $this = $(this);
        if ($this.css('max-height') == 'none') {
            $this.css('max-height', '500px');
        } else {
            $this.css('max-height', 'none');
        }
    });
});
$('.comment-like').click(function() {
    // console.log($(this).attr('data-id'))
    // console.log(document.domain)
    var data_id = $(this).attr('data-id')
    var result
    $.post('api/comment', {'post_id': data_id, 'comment_type': 1}, function(result) {
        // console.log(result)
        // console.log(this)
        // console.log($('[data-id=' + data_id + ']').filter('.comment-like'))
        // console.log($('.like-container [data-id=' + data_id + ']').next().text())
        console.log(result['msg'])
        if (result['status'] == 0) {
            //alert(result['msg'])
            $('.msg').fadeIn();
            $('.msg').fadeOut(2000);
        } else {
            $('.like-container [data-id=' + data_id + ']').next().text(result['msg'])
        }
    })
})
$('.comment-unlike').click(function() {
    // console.log($(this).attr('data-id'))
    // console.log(document.domain)
    var data_id = $(this).attr('data-id')
    var result
    $.post('api/comment', {'post_id': data_id, 'comment_type': 0}, function(result) {
        // console.log(result)
        // console.log(this)
        // console.log($('[data-id=' + data_id + ']').filter('.comment-like'))
        // console.log($('.like-container [data-id=' + data_id + ']').next().text())
        console.log(result['msg'])
        if (result['status'] == 0) {
            $('.msg').fadeIn();
            $('.msg').fadeOut(2000);
        } else {
            $('.unlike-container [data-id=' + data_id + ']').next().text(result['msg'])
        }
    })
})

// $('#img').on('change', function(){
//     var file = this.files[0];
//     console.log(file.size);
//     to_kb = file.size / 1024;
//     limit = to_kb / 1024;
//     if (limit > 3) {
//         alert('文件尺寸大于3MB')
//         return
//     }
//     fd = new FormData();
//     fd.append('username','michael');
//     fd.append('f1', file);
//     $.ajax({
//         type: 'POST',
//         url: 'upload/',
//         data: fd,
//         contentType:false,
//         processData:false,
//         success: function(result){
//             console.log(result);
//             var txt = $('#textbody')[0].value;
//             console.log(txt)
//             console.log(txt + '![](' + result + ')')
//             $('#textbody').val(txt + '\n' + '![](' + result + ')')
//             },
//         error: function(error) {
//             console.log(error)
//         }
//     })
// })
// $('#testbtn').click(function(){
//     $('#textbody').val('test');
// })

$('#inputGroupFileAddon02').click(function(){
        console.log($('#inputGroupFile02')[0].files)
        var txt = $('#textbody')[0].value;
        // $('#textbody').val(txt + '\n' + '![](' + 'url' + ')')
        var file = $('#inputGroupFile02')[0].files[0];
        to_kb = file.size / 1024;
        limit = to_kb / 1024;
        if (limit > 3) {
            alert('文件尺寸大于3MB')
            return
        }
        $('.custom-file-label').html("上传中。请稍候")
        fd = new FormData();
        fd.append('f1', file);
        $.ajax({
            type: 'POST',
            url: 'upload/',
            data: fd,
            contentType:false,
            processData:false,
            success: function(result){
                console.log(result);
                var txt = $('#textbody')[0].value;
                console.log(txt)
                console.log(txt + '![](' + result + ')')
                $('#textbody').val(txt + '\n' + '![](' + result + ')');
                $('.custom-file-label').html("上传图片完成")
                },
            error: function(error) {
                console.log(error)
            }
        })
    })
$('.custom-file-input').on('change', function(){
    var filename = this.files[0].name;
    console.log(filename)
    $('.custom-file-label').html(filename)
})
$(document).ready(function(){
    $('.text-body img').each(function(){
        var link = this.src;
        $(this).before('<br>' + "<a href=" + link+ ">[查看原图]</a>" + '<br>')
    })
    //console.log($('.text-body img').before('<br>' + "<a>[查看原图]</a>" + '<br>'))
})