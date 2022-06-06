
<html>
<head>
<title> FeedBack Page</title>
<style>
body {
	background-image : url('/static/covid.jpg');
}
ul{
	text-align: justify;
	list-style-position: inside;
}
.container1{
	display:flex;
}
.container1 > div{
	margin: 10px;
	padding: 20px;
	font-size : 18px;
}
.feedback-form{
	text-align:center;
	color:white;
}
p{
	text-align:	left;
	padding-left:15%;
}
h2{
	color:orange;
}

</style>
   </head>
<body>
<?php
  $name = $_POST['name'];
  $email_from = $_POST['email'];
  $feedback = $_POST['feedback'];
  $suggestion = $_POST['suggestion'];
  $email_subject = "New Form submission";
  $email_body = "You have received a new feedback from the user $name.\n"."Here is the feedback:\n $feedback".
  $to = "jeyasurya1210@gmail.com";
  $header = "From: $email_from \r\n";
  mail($to,$email_subject,$email_body,$header);
  echo $name;
?>
<marquee style="color:red; font-size:50px; text-shadow: 1px 1px #ffe5e5;">Feedback</marquee>
<div class="container1">
<div>
<h2> Covid-19 Precautions </h2>
<ul style="color:White">
<li>Maintain a safe distance from others (at least 1 metre), even if they don't appear to be sick.</li>
<li>Wear a mask in public, especially indoors or when physical distancing is not possible.</li>
<li>Choose open, well-ventilated spaces over closed ones. Open a window if indoors.</li>
<li>Clean your hands often. Use soap and water, or an alcohol-based hand rub.</li>
<li>Get vaccinated when it’s your turn. Follow local guidance about vaccination.</li>
<li>Cover your nose and mouth with your bent elbow or a tissue when you cough or sneeze.</li>
<li>Stay home if you feel unwell.</li>
</ul>
<br>
<h2> Covid-19 Symptoms </h2>
<ul style="color:White">
<li>Fever</li>
<li>cough</li>
<li>tiredness</li>
<li>loss of taste or smell</li>
<li>sore throat</li>
<li>difficulty breathing or shortness of breath</li>
<li>loss of speech or mobility, or confusion</li>
<li>chest pain</li>
</ul>
</div>

</div>

<center>
<p style="color:White" >For further more queries contact us  <a style="color:Orange"  href="mailto:dhacus7@gmail.com">Send email</a></p>
</center>
	
</body>
</html>