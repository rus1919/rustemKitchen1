$(function() {

	$(window).scroll(function() {
		var headerHeight = $('.header').outerHeight();
		if ($(window).scrollTop() > headerHeight) {
			$('.form').addClass('scrolled');
		} else {
			$('.form').removeClass('scrolled');
		}
	});

	$('.scroll-link').click(function(event) {
		event.preventDefault();
		var id  = $(this).attr('href'),
		top = $(id).offset().top;
		$('body,html').animate({scrollTop: top}, 500);
	});

	$('.header__navbar').click(function() {
		$('.menu').slideToggle(300);
		return false;
	});

	$(document).mouseup(function (e){
		var div = $(".menu, .header__navbar");
		if (!div.is(e.target)
		    && div.has(e.target).length === 0) {
			$('.menu').slideUp(300);
		}
	});

	$('.header__search-link').click(function() {
		$('.header__search').addClass('active');
	});

	$(document).mouseup(function (e){
		var div = $(".header__search");
		if (!div.is(e.target)
		    && div.has(e.target).length === 0) {
			$('.header__search').removeClass('active');
		}
	});

	$('.modal-link').click(function() {
		var modal = $(this).attr('href');
		$(modal).fadeIn(300);
		return false;
	});

	$('.modal__close, .modal__blackout').click(function() {
		$(this).parents('.modal-wrapper').fadeOut(300);
		return false;
	});

	$('.chat-link').click(function() {
		$('.chat').fadeToggle(100);
		return false;
	});

	$('.header__private-info').click(function() {
		return false;
	});
});