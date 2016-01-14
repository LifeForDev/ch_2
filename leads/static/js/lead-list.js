// Used to receive csrftoken, to use in ajax calls
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

$(document).ready(function() {
    $.ajaxSetup({
        headers: { "X-CSRFToken": getCookie("csrftoken") }
    });
    $("body").delegate('.lead-delete', 'click', function(event) {
        if(confirm("Are you sure you want to delete this Lead?")) {
            event.preventDefault();
            var del_url = $(event.target).data('url');
            $.ajax({
                url: del_url,
                method: 'post',
                success: function() {
                    location.reload();
                }
            });
        }
    });

    $("body").delegate('.select-all', 'click', function(event) {
        var checked = $(event.target).prop('checked');
        $('.check-selected').each(function() {
           $(this).prop('checked', checked);
        });
    });

    $("body").delegate('.batch-delete', 'click', function(event) {
        if(confirm("Are you sure you want to delete selected Leads?")) {
            // Prepare list for deletion
            var ids = [];
            $('.check-selected:checked').each(function() {
               ids.push($(this).data('id'));
            });

            // Delete
            $.ajax({
                url: '/leads/batch_delete/',
                method: 'post',
                data: {
                    'ids': ids
                },
                success: function() {
                    location.reload();
                }
            })
        }
    });
});
