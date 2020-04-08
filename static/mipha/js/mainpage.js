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