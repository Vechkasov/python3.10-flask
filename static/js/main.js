$(document).ready(function(){
    $(window).on('load',function(){
        $('#mymodal').modal('show');

        setTimeout(()=>$('#mymodal').modal('hide'), 4000);
    });

    $(document).on("click", "#clear_notifications", function(){

        $.ajax({
            type: 'GET',
            url: '/notifications/delete',
            dataType: 'text',
            error: function(data){
                console.log(data);
            }
        });

        location.reload()
    })

});