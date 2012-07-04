$(document).ready(function () {
    // bind submit button click
    $(":submit").click(submitquote);
	// fix sub nav on scroll
	var $win = $(window)
	  , $nav = $('.subnav')
	  , navTop = $('.subnav').length && $('.subnav').offset().top - 40
	  , isFixed = 0
            //, brand_margin = -150

	processScroll()

	$nav.on('click', function () {
	      if (!isFixed) setTimeout(function () {  $win.scrollTop($win.scrollTop() - 47) }, 10)
	    })
	
	$win.on('scroll', processScroll)

	function processScroll() {
	  var i, scrollTop = $win.scrollTop()
      /*var new_margin = brand_margin + scrollTop
      if (new_margin > 0) {
          new_margin = 0
      }
      console.log(new_margin)
      $(".brand").css("margin-left", new_margin)*/
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
            $(".modal-body").prepend('<div class="alert alert-success">Thanks! We\'ll contact you soon.</div>')
            $(".form-body, :submit, .modal-footer p, .modal-body p").slideUp('fast', function() {
                window.setTimeout(function() {
                    $("#modal-close").click()
                    window.setTimeout(function() {
                        $("#modal-request").html(data.html)
                        $(":submit").click(submitquote)
                    }, 1500)
                }, 2000)
            })
        }
    });
    return false
}