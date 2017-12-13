$(document)
    .ready(function () {

        $('button#tenant')
            .unbind()
            .click(function (event) {
                event.preventDefault()
                select = {
                    'Tenant': 1
                }
                console.log(select)
                $.ajax({
                    'url': '/ajax/landlord/tenant/',
                    'type': 'POST',
                    'data': select,
                    'dataType': 'json',
                    'success': function (data) {
                        alert("success");
                    }

                })
            });

        $('#landlord')
            .unbind()
            .click(function (event) {
                event.preventDefault()
                select = {
                    'LandLord': 2
                }

                $.ajax({
                    'url': '/ajax/landlord/tenant/',
                    'type': 'POST',
                    'data': select,
                    'dataType': 'json',
                    'success': function (data) {
                        alert("success");
                        window.location.href="/index.html";
                    }
                })
                console.log("what is")
            })
    });