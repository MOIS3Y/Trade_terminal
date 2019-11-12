// Update Exchange Accounts div 
// $(document).ready(function() {
//     $('#btn').click(function() { setTimeout(function() {
//         $.ajax({
//             url: "/service",
//             type: "POST",
//             success: function(resp) {
//                 $('div#response').replaceWith(resp.data);
//             }
//         });}, 3000);
//     }); 
// });


// $(document).ready(function() {
//     $('#btn').click(function() {
//         $.ajax({
//                 url: '/service',
//                 type: 'POST',
//                 data: {
//                     exchange_id: $('#exchange_id').val(),
//                     name: $('#name').val(),
//                     secret_key: $('#secret_key').val(),
//                     public_key: $('#public_key').val()
//                 },
//                 success: function(resp) {
//                     $('div#response').replaceWith(resp.data);
//                 }
//             })
//             .done(function(data) {
//                 console.log(data);
//             })
//             .fail(function() {
//                 console.log("error");
//             })
//             .always(function() {
//                 console.log("complete");
//             });

//         event.preventDefault();

//     });

// });