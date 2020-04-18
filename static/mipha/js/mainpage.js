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
    $.post('/api/comment', {'post_id': data_id, 'comment_type': 1}, function(result) {
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
    $.post('/api/comment', {'post_id': data_id, 'comment_type': 0}, function(result) {
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
        if (limit > 5) {
            alert('文件尺寸大于5MB')
            return
        }
        $('.custom-file-label').html("上传中。请稍候")
        fd = new FormData();
        fd.append('f1', file);
        $.ajax({
            type: 'POST',
            url: '/upload/',
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
    //console.log(alert(post))
})

$('.comment-btn').click(function(){
    var comment_btn = $(this)
    var postid = $(this).data('id');
    var container = $('#comment-container-' + postid);
    console.log(container)
    if (container.attr('style') == 'display: block;') {
        console.log('yes')
        container.css('display', 'none');
    } else if (container.attr('style') == 'display: none;'){
        container.css('display', 'block');
    } else {
        // 画出评论框
        var li = $(this).closest('li');
        var row = li.find('.row');
        
        var divwrapper = $('<div class="comment-container" id="comment-container-' + postid + '" style="display: block;"></div>')
        var form = $('<form action="/api/newcomment/" method="POST" id="newcommentform"></form>')
        var nicknamewrapper = $('<div class="form-group row"></div>')
        var nicknamebar = $('<label for="author" class="col-sm-2 col-form-label">用户名</label>')
        var nicknameinput = $('<div class="col-sm-10"><input type="text" class="form-control" id="authorinput" name="author" placeholder="输入用户名" required></div>')
        var txtarea = $('<div class="input-group"><textarea id="comment-textbody" class="form-control" aria-label="With textarea" required></textarea></div>')
        var btn = $('<button type="submit" class="btn btn-secondary btn-lg btn-block" id="submit">提交</button>')
        nicknamewrapper.append(nicknamebar)
        nicknamewrapper.append(nicknameinput)
        form.append(nicknamewrapper)
        form.append(txtarea)
        // divwrapper.append(form)
        // divwrapper.append(btn)
        //row.after(divwrapper)

        // 先获取该post下的评论数量，按照数量画出相应的评论框
        var ol = $('<ol class="comment-list"></ol>')
        $.ajax({
            url: '/api/getcomment/' + postid,
            type: 'GET',
            success:function(get_result){
                for (var i in get_result.comments){
                    var author = get_result.comments[i].comment_author;
                    var pub_date = get_result.comments[i].comment_date;
                    var content = get_result.comments[i].comment_content;
                    var postid = get_result.comments[i].comment_post_id;

                    var com_li = $('<li class="comment-list-row"></li>')
                    var li_author_div = $('<div class="comment-author-container"><span class="comment-author">' + author + '</span><span class="comment-date">' + pub_date + '</span></div>')
                    var li_content_div = $('<div class="comment-content">' + content + '</div>')
                    // var li_floor_div = $('<div class="comment-floor">#' + i + '楼</div>')
                    com_li.append(li_author_div)
                    com_li.append(li_content_div)
                    // com_li.append(li_floor_div)
                    ol.append(com_li)
                }
                divwrapper.append(ol)
                divwrapper.append(form)
                divwrapper.append(btn)
                row.after(divwrapper)
            }
        })
        
        // 点击发布后
        btn.click(function(){
            var t = $(this);

            var content_div = t.parent().parent();

            var author = content_div.find('input#authorinput').val()
            var txt = content_div.find('textarea#comment-textbody').val()

            // 验证
            if (author == '' || author == null){
                $('#authorinput').focus();
                return false;
            } else if (txt == '' || txt == null) {
                $('#comment-textbody').focus();
                return false;
            }

            var post_id = content_div.find('span.textright a').html()
            $.ajax({
                url: '/api/newcomment',
                type: 'POST',
                data: {
                    'author': author,
                    'content': txt,
                    'post_id': post_id,
                },
                success:function(result){
                    var com_li = $('<li class="comment-list-row"></li>')
                    var li_author_div = $('<div class="comment-author-container"><span class="comment-author">' + result.author + '</span><span class="comment-date">' + result.date + '</span></div>')
                    var li_content_div = $('<div class="comment-content">' + result.content + '</div>')
                    com_li.append(li_author_div)
                    com_li.append(li_content_div)
                    ol.append(com_li)
                    var c = comment_btn.html()[4];
                    c = parseInt(c);
                    c += 1;
                    comment_btn.html('评论区['+ c + ']')
                }
            })
            t.prop("disabled", true);
            content_div.find('textarea#comment-textbody').val('')
            setTimeout(function(){
                t.prop("disabled", false);
            }, 5000)
        })
    }

    

    // $.ajax({
    //     url:''
    // })
    // if ($('#comment-' + data_id).css('display') == 'none') {
    //     $('#comment-' + data_id).css('display', 'block')
    // } else {
    //     $('#comment-' + data_id).css('display', 'none')
    // }
})

