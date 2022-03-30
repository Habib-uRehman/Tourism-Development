// Director field form addition
$(document).ready(function() {
    var max_fields = 10; //maximum input boxes allowed
    var wrapper = $(".director-input-field"); //Fields wrapper
    var add_button = $(".add-director-field"); //Add button ID

    var x = 1; //initlal text box count
    $(add_button).click(function(e) { //on add input button click
        e.preventDefault();
        if (x < max_fields) { //max input box allowed
            x++; //text box increment
            $(wrapper).append('<div class="row"> <div class="col-3 my-2"> <label class="form-label">Name</label>  <input type="text" class="form-control" name=""/></div>  <div class="col-3 my-2"> <label class="form-label">Address</label>  <input type="text" class="form-control" name=""/></div> <div class="col-3 my-2"> <label class="form-label">Year Of Experiance</label>  <input type="text" class="form-control" name=""/></div> <div class="col-3 my-2"> <label class="form-label">Qualification</label>  <input type="text" class="form-control" name=""/></div> <a href="#" class="remove_field">Remove</a></div>'); //add input box
        }
    });

    $(wrapper).on("click", ".remove_field", function(e) { //user click on remove text
        e.preventDefault();
        $(this).parent('div').remove();
        x--;
    })
});



// Manager field form addition
$(document).ready(function() {
    var max_fields = 10; //maximum input boxes allowed
    var wrapper = $(".manager-input-field"); //Fields wrapper
    var add_button = $(".add-manager-field"); //Add button ID

    var x = 1; //initlal text box count
    $(add_button).click(function(e) { //on add input button click
        e.preventDefault();
        if (x < max_fields) { //max input box allowed
            x++; //text box increment
            $(wrapper).append('<div class="row"> <div class="col-3 my-2"> <label class="form-label">Name</label>  <input type="text" class="form-control" name=""/></div>  <div class="col-3 my-2"> <label class="form-label">Address</label>  <input type="text" class="form-control" name=""/></div> <div class="col-3 my-2"> <label class="form-label">Year Of Experiance</label>  <input type="text" class="form-control" name=""/></div> <div class="col-3 my-2"> <label class="form-label">Qualification</label>  <input type="text" class="form-control" name=""/></div> <a href="#" class="remove_field">Remove</a></div>'); //add input box
        }
    });

    $(wrapper).on("click", ".remove_field", function(e) { //user click on remove text
        e.preventDefault();
        $(this).parent('div').remove();
        x--;
    })
});



// Partner field form addition
$(document).ready(function() {
    var max_fields = 10; //maximum input boxes allowed
    var wrapper = $(".partner-input-field"); //Fields wrapper
    var add_button = $(".add-partner-field"); //Add button ID

    var x = 1; //initlal text box count
    $(add_button).click(function(e) { //on add input button click
        e.preventDefault();
        if (x < max_fields) { //max input box allowed
            x++; //text box increment
            $(wrapper).append('<div class="row"> <div class="col-3 my-2"> <label class="form-label">Name</label>  <input type="text" class="form-control" name=""/></div>  <div class="col-3 my-2"> <label class="form-label">Address</label>  <input type="text" class="form-control" name=""/></div> <div class="col-3 my-2"> <label class="form-label">Year Of Experiance</label>  <input type="text" class="form-control" name=""/></div> <div class="col-3 my-2"> <label class="form-label">Qualification</label>  <input type="text" class="form-control" name=""/></div> <a href="#" class="remove_field">Remove</a></div>'); //add input box
        }
    });

    $(wrapper).on("click", ".remove_field", function(e) { //user click on remove text
        e.preventDefault();
        $(this).parent('div').remove();
        x--;
    })
});



// owner field form addition
$(document).ready(function() {
    var max_fields = 10; //maximum input boxes allowed
    var wrapper = $(".owner-input-field"); //Fields wrapper
    var add_button = $(".add-owner-field"); //Add button ID

    var x = 1; //initlal text box count
    $(add_button).click(function(e) { //on add input button click
        e.preventDefault();
        if (x < max_fields) { //max input box allowed
            x++; //text box increment
            $(wrapper).append('<div class="row">  <div class="col-lg-4 col-md-6 my-2"> <label for="" class="form-label">Name of Owner:</label> <input type="text" class="form-control" /> </div><div class="col-lg-2 col-md-6 my-2"><label for="" class="form-label">Owner % :</label><input type="text" class="form-control" /></div> <div class="col-lg-6 col-md-12 my-2"><label for="" class="form-label">Full Address of Owner:</label><input type="text" class="form-control" /></div><div class="col-lg-6 col-md-12 my-2"><label for="" class="form-label">Telegraphic Address of Owner:</label><input type="text" class="form-control" /> </div><div class="col-lg-3 col-md-6 my-2"> <label for="" class="form-label">Owner Telephone Number:</label> <input type="text" class="form-control" /></div><a href="#" class="remove_field">Remove</a></div>'); //add input box
        }
    });

    $(wrapper).on("click", ".remove_field", function(e) { //user click on remove text
        e.preventDefault();
        $(this).parent('div').remove();
        x--;
    })
});


// Hotel Manager field form addition
$(document).ready(function() {
    var max_fields = 10; //maximum input boxes allowed
    var wrapper = $(".hotelManager-input-field"); //Fields wrapper
    var add_button = $(".add-hotelManager-field"); //Add button ID

    var x = 1; //initlal text box count
    $(add_button).click(function(e) { //on add input button click
        e.preventDefault();
        if (x < max_fields) { //max input box allowed
            x++; //text box increment
            $(wrapper).append('<div class="row"><div class="col-lg-4 col-md-6 my-2"> <label for="" class="form-label">Name of Manager:</label> <input type="text" class="form-control" /> </div> <div class="col-lg-2 col-md-6 my-2 text-nowrap"> <label for="" class="form-label">Manager % :</label> <input type="text" class="form-control" />  </div> <div class="col-lg-6 col-md-12 my-2"> <label for="" class="form-label">Manager Adress:</label> <input type="text" class="form-control" />  </div> <div class="col-lg-3 col-md-12 my-2"><label for="" class="form-label">Manager Telephone Number:</label><input type="text" class="form-control" /></div><a href="#" class="remove_field">Remove</a> </div>'); //add input box
        }
    });

    $(wrapper).on("click", ".remove_field", function(e) { //user click on remove text
        e.preventDefault();
        $(this).parent('div').remove();
        x--;
    })
});