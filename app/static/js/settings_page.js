$(document).ready(function() {
    // Create new exchange account:
    $('#new_account').submit(function(event) {
        event.preventDefault();
        var exchange_id = $('#exchange_id').val();
        var name = $('#name').val();
        var secret_key = $('#secret_key').val();
        var public_key = $('#public_key').val();

        if (exchange_id === "" || name === "" || secret_key === "" || public_key === "") {
            $('#new_account').addClass('was-validated');
        } else {
            $.ajax({
                    url: '/update_accounts',
                    type: 'POST',
                    data: {
                        update: 'create_account',
                        exchange_id: exchange_id,
                        name: name,
                        secret_key: secret_key,
                        public_key: public_key
                    },
                    success: function(response) {
                        $('#accounts_table').replaceWith(response.accounts);
                        $('#new_account').removeClass('was-validated');
                    }
                })
                .done(function(response) {
                    console.log(response.status);
                })
                .fail(function() {
                    console.log("error");
                })
                .always(function() {
                    console.log('done');
                });
        }
    });
    // Open Modal for confirmation of delete account
    $('#accounts').on('click', '.del_button', function(event) {
        $('#yes-delete').val($(this).val());
        var modal = $('#confirmation_del')
        var modal_title = $(this).data('whatever')
        modal.find('.modal-title').text(modal_title)
        event.preventDefault();
    });
    // Delete account
    $('.modal-footer').on('click', '#yes-delete', function() {
        console.log('click del button: ', $('#yes-delete').val());
        $(this).data('clicked', true);
        if ($('#yes-delete').data('clicked')) {
            $.ajax({
                    url: '/update_accounts',
                    type: 'POST',
                    data: {
                        'update': 'delete_account',
                        id_account: $('#yes-delete').val()
                    },
                    success: function(response) {
                        $('#accounts_table').replaceWith(response.accounts);
                    }
                })
                .done(function(response) {
                    console.log(response.status);
                })
                .fail(function() {
                    console.log("error");
                })
                .always(function() {
                    console.log("complete");
                });
        }
    });
});
