function addForm(type) {
    var form_idx = $('#id_'+type+'-TOTAL_FORMS').val();
    $('#'+type).append($('#formset-template').html().replace(/__prefix__/g, form_idx));

    $('#id_'+type+'-TOTAL_FORMS').val(parseInt(form_idx) + 1);
}

function removeForm(type, elem) {
    var elem_id = elem.data('id');

    // Mark form for deletion
    elem.find('#id_'+type+'-'+elem_id+'-DELETE').val("1");
    elem.hide();
}

$(document).ready(function() {
    // Change language inline template to contain remove button instead of add
    // Replace add button if page reloaded after submit
    var removeBtn = '<button class="btn remove-form"><i class="fa fa-remove fa-fw"></i>Remove</button>';
    $('#formset-template').find('.input-group-btn').html(removeBtn);
    $('#languages > .formset-languages > .input-group > .input-group-btn').slice(1).html(removeBtn);

    $("body").delegate('.add-form', 'click', function(event) {
        event.preventDefault();
        addForm('languages');
    });

    $("body").delegate('.remove-form', 'click', function(event) {
        event.preventDefault();
        var element = $(event.target).closest('.formset-languages');
        removeForm('languages', element);
    });
});
