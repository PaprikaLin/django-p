$(document).ready(function() {
    $('.post-list li a').click(function(event){
        event.preventDefault();
        $('#ajaxbody').load(this.href)
    })
}) 