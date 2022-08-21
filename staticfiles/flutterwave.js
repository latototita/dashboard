const form = document.getElementById("payForm")
//document.getElementById("")
form.addEventListener("submit",payNow);

function payNow(e) {
	// prevent Normal form submit
	e.preventDefault();

	//set configurations
	FlutterwaveChectout({
		public_key:"",
		tx_ref:"Adsket"+Math.floor((Math.random()*1000000000)+1),
		amount:document.getElementById("amount").value,
		currency:document.getElementById("currency").value,
		customer:{
			email:document.getElementById("email").value,
			phonenumber:document.getElementById("phoneNumber").value,
			name:document.getElementById("name").value,
		},
		callback:function(data){
			//console.log(data);
			const reference=data.tx_ref;
			$.ajax({
		        type: "POST",
		        url: '/payment',
		        data: {
		            "result": data,
		        },
		        dataType: "json",
		        success: function (data) {
		            // any process in data
		            alert("successfull")
		        },
		        failure: function () {
		            alert("failure");
		        }
		    });
		}
	
	})
	
}