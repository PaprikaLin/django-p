$(document).ready(function() {
    $('.post-title a').click(function(event){
        event.preventDefault();
        $('#ajaxbody').load(this.href)
    })
}) 