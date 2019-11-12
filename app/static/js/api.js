// Add new exchange account:
$(document).ready(function() {
    $('#new_account').on('submit', function(event) {
        $.ajax({
                url: '/new_account',
                type: 'POST',
                data: {
                    exchange_id: $('#exchange_id').val(),
                    name: $('#name').val(),
                    secret_key: $('#secret_key').val(),
                    public_key: $('#public_key').val()
                },
                success: function(response) {
                    $('div#newacc').replaceWith(response.newacc);
                    // $('div#acc_modal').replaceWith(response.acc_modal);
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

        event.preventDefault();

    });

});


// Delete exchanges accounts:
$(document).ready(function() {
    $('.del_button').on('click', function(event) {
        $.ajax({
                url: '/delete_account',
                type: 'POST',
                data: {
                    id_account: $(this).val()
                },
                success: function(response) {
                    $('div#newacc').replaceWith(response.data);
                    // $('div#acc_modal').replaceWith(response.acc_modal);

                }
            })
            .done(function(response) {
                console.log(response.status, response.data);
            })
            .fail(function() {
                console.log("error");
            })
            .always(function() {
                console.log("complete");
            });

        event.preventDefault();

    });

});


// $(document).ready(function() {
//     $('#close').click(function(event) {
//         alert('TEST');
//     });
// });