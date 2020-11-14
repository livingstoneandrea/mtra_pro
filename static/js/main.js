$(document).ready(function() {
    var nav_offset_top = $('header').height() + 50;
    //* Navbar Fixed
    function navbarFixed() {
        if ($('#app-header').length) {
            $(window).scroll(function() {
                var scroll = $(window).scrollTop();
                if (scroll >= nav_offset_top) {
                    $('#app-header').addClass('navbar_fixed');
                } else {
                    $('#app-header').removeClass('navbar_fixed');
                }
            });
        }
    }
    navbarFixed();

    document.querySelector('#navbar-toggler').addEventListener('click', (e) => {
        e.preventDefault();
        // $(this).toggleClass('is-active');
        $('.navbar-menu, .hamburger').toggleClass('is-active');

    });
    $('.navbar-item').on('click', (e) => {
        $('.navbar-menu, .hamburger').toggleClass('is-active');
    });

    $(window).scroll(function() {
        var height = $(window).scrollTop();
        if (height > 100) {
            $("#back-top").fadeIn();
        } else {
            $("#back-top").fadeOut();
        }
    });
    $("#back-top").click(function(e) {
        e.preventDefault();
        $("html,body").animate({
                scrollTop: 0
            },
            "slow"
        );
        return false;
    });


});