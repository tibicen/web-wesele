$(document).on("scroll", onScroll);

function onScroll(event) {

  var scrollPosition = $(document).scrollTop();

  $(".nav-link").each(function () {
    var currentLink = $(this);
    var refElement = $(currentLink.attr("href"));
    var siblings = currentLink.closest("li").siblings();
    var targetOffset = refElement.offset().top - 70;
    if (scrollPosition >= targetOffset) {
      currentLink.addClass("active");
      siblings.find(".nav-link").removeClass("active");
    }
  });
}

$(function () {
  var speed = 800;
  var topOffset = 0;
  var currentLink = $(this);
  var siblings = currentLink.closest("li").siblings();
  // console.log(currentLink)
  $("body").on("click", ".nav-link", function (event) {
    var amountToScroll = ($(this.hash).offset().top) - topOffset;
    event.preventDefault();
    $("html, body").animate({ scrollTop: amountToScroll }, speed);
    currentLink.addClass("active");
    siblings.find(".nav-link").removeClass("active");
  });
  $("body").on("click", ".arrow-down", function (event) {
    var amountToScroll = ($(this.hash).offset().top) - topOffset;
    event.preventDefault();
    $("html, body").animate({ scrollTop: amountToScroll }, speed);
  });
});
