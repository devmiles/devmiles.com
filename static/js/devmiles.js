$(document).ready(function () {
    // bind submit button click
    $(":submit").click(submitquote);
	// fix sub nav on scroll
	var $win = $(window)
	  , $nav = $('.subnav')
	  , navTop = $('.subnav').length && $('.subnav').offset().top - 40
	  , isFixed = 0

	processScroll()

	$nav.on('click', function () {
	      if (!isFixed) setTimeout(function () {  $win.scrollTop($win.scrollTop() - 47) }, 10)
	    })
	
	$win.on('scroll', processScroll)

	function processScroll() {
	  var i, scrollTop = $win.scrollTop()
	  if (scrollTop >= navTop && !isFixed) {
	    isFixed = 1
	    $nav.addClass('subnav-fixed')
	  } else if (scrollTop <= navTop && isFixed) {
	    isFixed = 0
	    $nav.removeClass('subnav-fixed')
	  }
	}
	$('section [href^=#]').click(function (e) {
	      e.preventDefault()
	    })
});

var submitquote = function()
{
    $.post('/quote', $(".form-horizontal").serialize(), function(data) {
        console.log(data)
        if (data.status == 'error') {
            $("#modal-request").html(data.html)
            $(":submit").click(submitquote)
        } else if (data.status == 'ok') {
            $("#modal-request").html(data.html)
        }
    });
    return false
}