$(function() {

  // --- header/nav 関連 ---

  // panel-nav の表示・非表示
  $('#js-header__panel-button').on('click touched', function(){$('#js-panel').toggle();});
  $("body").on('click touched', function (event) {
    if ($(event.target).attr('id') != 'js-header__panel-button'
        && !$(event.target).closest('#js-panel-nav').length) {
      $('#js-panel').hide();
    }
  });

  // panel-nav の絞り込みボタンクリック時
  $('.js-panel-nav__menu-item').on('click touched', function () {
    $(this).siblings().removeClass('panel-nav__menu-item--checked');
    $(this).siblings().find('.js-panel-nav__button[checked=checked]').attr('checked', false);
    $(this).addClass('panel-nav__menu-item--checked').find('.js-panel-nav__button').attr('checked', true);
  });
});
