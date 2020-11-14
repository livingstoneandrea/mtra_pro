$(document).ready(function() {

    new PerfectScrollbar(document.querySelector('.sidebar-content'), {
        wheelSpeed: 10,
        wheelPropagation: !0,
        minScrollbarLength: 5
    });
    var hideSideBar = function() {
        $('.app-sidebar').addClass("hide-sidebar");

    };
    var openSideBar = function() {

        $('.app-sidebar').removeClass("hide-sidebar");
    };

    $(".search-btn").on('click', function() {
        $(".header-search").addClass('open');
        $('.header-search .input-group .form-control').animate({
            'width': '200px',
        });
    }), $(".search-close").on('click', function() {
        $('.header-search .input-group .form-control').animate({
            'width': '0',
        });
        setTimeout(function() {
            $(".header-search").removeClass('open');
        }, 300);
    });

    $('.create').on('click', function() {
        $(".dropdown_menu").toggleClass('show');
    });
    $('.acc-opt_toggler').on('click', function() {
        $(".dropdown").toggleClass('is-active');
    });



    var body = $('body'),
        sidebar = $('.sidebar-content');

    sidebar.hover(function() {
            $('body').css({ 'overflow': 'hidden', 'transition': 'all 0.4s ease' });
        },
        function() {
            $('body').css({ 'overflow': 'auto', 'transition': 'all 0.4s ease' });
        });


    $('.sidebar-content').on('click', '.navigation-main .nav-item a', function() {
        var e = $(this).parent(".nav-item");
        if (e.hasClass("has-sub") && e.hasClass("open")) {
            //remove some classess
            $(this).css("display", "");
            $(this).find(".menu-item").removeClass("is-shown");
            e.removeClass("open");
        } else {
            if (e.hasClass("has-sub")) {
                var a = e.children(".submenu-content"),
                    n = a.children(".menu-item").addClass("is-hidden");

                e.addClass("open");
                a.hide().slideDown(200, function() {
                    $(this).css("display", "");
                });
                setTimeout(function() {
                    n.addClass("is-shown");
                    n.removeClass("is-hidden");
                }, 0);
                
                $(".sidebar-content").data("collapsible");

            }
            return !1;
        }

    });


    if ($(window).width() < 992) {
        hideSideBar();

    } else {
        openSideBar();

    }

    $(window).resize(function() {
        if ($(window).width() < 992) {
            hideSideBar();
        } else {
            openSideBar();
        }
    });
    $(".navigation-main .nav-item.open").on("click", ".navigation li:not(.has-sub)", function() {
        if ($(window).width() < 992) {
            hideSideBar();
        }
    });
    $(".navigation-main .nav-item.open").on("click", ".logo-text", function() {
        if ($(window).width() < 992) {
            hideSideBar();
        }
    });
    $(".mobile-nav-toggle").on("click", function(e) {
        if ($(window).width() < 992) {
            e.stopPropagation();
            $(".app-sidebar").toggleClass("hide-sidebar");

        }
    });
    $("html").on("click", function(s) {
        $(window).width() < 992 && ($(".app-sidebar").hasClass("hide-sidebar") || 0 !== $(".app-sidebar").has(s.target).length || $(".app-sidebar").addClass("hide-sidebar"));

    });
    $("#sidebarClose").on("click", function() {
        hideSideBar();
    });
    $('.submenu-content a.menu-item').on('click',function(event){
        event.preventDefault();
    
        console.log($(this).attr('href'));
        window.location.href = $(this).attr('href') === undefined ? '': $(this).prop('href').toString();
    })

    // tabs
    document.querySelectorAll("ul.custom-pills > li.nav-item a").forEach(item => {
        item.addEventListener('click', function(e) {
            e.preventDefault();
            console.log($(this).attr('href'));
            openTabLink(e, $(this).attr('href').slice(1));

        });
    });


    function openTabLink(e, tabName) {
        // Declare all variables
        var i, tabcontent, tablinks;

        // Get all elements with class="tab-pane" and hide them
        tabcontent = document.getElementsByClassName("tab-pane");
        for (i = 0; i < tabcontent.length; i++) {
            tabcontent[i].style.display = "none";
        }

        // Get all elements with class="nav-link" and remove the class "active"
        tablinks = $("ul.custom-pills > li.nav-item > a.nav-link");
        for (i = 0; i < tablinks.length; i++) {
            tablinks[i].className = tablinks[i].className.replace("active", "");
        }

        // Show the current tab, and add an "active" class to the link that opened the tab
        document.getElementById(tabName).style.display = "block";
        e.currentTarget.className += " active";
    }

    var acc = document.getElementsByClassName("accordion");
    var i;

    for (i = 0; i < acc.length; i++) {
        acc[i].addEventListener("click", function() {
            /* Toggle between adding and removing the "active" class,
            to highlight the button that controls the panel */
            this.classList.toggle("active");

            /* Toggle between hiding and showing the active panel */
            var panel = this.nextElementSibling;
            if (panel.style.display === "block") {
                panel.style.display = "none";
            } else {
                panel.style.display = "block";
            }
        });
    }

    $('#del_acc').on('click',(e)=>{
        // e.preventDefault();
        const remove_url = $('#del_acc').attr('data-delete_url')
        console.log(remove_url)
        if(confirm('Are you sure you wanna delete your account?')){
            $.ajax({
                url: remove_url,
                dataType: "json",
                method: 'get',
                success: function(response) {
                    var msg = response["message"];
                    alert(msg);
                   
                },
                error: function(response) {
                    alert(response["errors"]);

                }
            }); 

        }else{
            console.log('process aborted');
        }
    })

});