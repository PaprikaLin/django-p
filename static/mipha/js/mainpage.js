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
