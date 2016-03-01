var headers = $('.headers')
$(document).on('scroll', function() {
	console.log($('.headers').offset());
	console.log(window.scrollY);
	if (window.scrollY > headers.height()) {
		headers.addClass('pinned-headers');
	} else {
		headers.removeClass('pinned-headers');
	}
});
