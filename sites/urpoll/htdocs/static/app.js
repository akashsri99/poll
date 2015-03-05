
  (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
  (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
  m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
  })(window,document,'script','//www.google-analytics.com/analytics.js','ga');

  ga('create', 'UA-60074856-1', 'auto');
  ga('send', 'pageview');

     function statusChangeCallback(response) {
    console.log('statusChangeCallback');
    console.log(response);
    // The response object is returned with a status field that lets the
    // app know the current login status of the person.
    // Full docs on the response object can be found in the documentation
    // for FB.getLoginStatus().
    if (response.status === 'connected') {
      // Logged into your app and Facebook.
      testAPI();
    } else if (response.status === 'not_authorized') {
      // The person is logged into Facebook, but not your app.
      document.getElementById('status').innerHTML = 'Please log ' +
        'into this app.';
    } else {
      // The person is not logged into Facebook, so we're not sure if
      // they are logged into this app or not.
      document.getElementById('status').innerHTML = 'Please log ' +
        'into Facebook.';
    }
  }

  function checkLoginState() {
    FB.getLoginStatus(function(response) {
      statusChangeCallback(response);
    });
  }
  window.fbAsyncInit = function() {
    FB.init({
      appId      : '1580592518848163',
      xfbml      : true,
      version    : 'v2.2'
    });
  };

  (function(d, s, id){
     var js, fjs = d.getElementsByTagName(s)[0];
     if (d.getElementById(id)) {return;}
     js = d.createElement(s); js.id = id;
     js.src = "//connect.facebook.net/en_US/sdk.js";
     fjs.parentNode.insertBefore(js, fjs);
   }(document, 'script', 'facebook-jssdk'));
  FB.getLoginStatus(function(response) {
  if (response.status === 'connected') {
    console.log(response.authResponse.accessToken);
  }
});
  function testAPI() {
    console.log('Welcome!  Fetching your information.... ');
    FB.api('/me', function(response) {
      console.log('Successful login for: ' + response.name);
      document.getElementById('status').innerHTML =
        'Thanks for logging in, ' + response.name + response.id +'!';
    });
  }

  <!-- fb script ends  -->
  <!--Google search -->
           (function() {
            var cx = '008331300526394667015:aopiaeht0be';
            var gcse = document.createElement('script');
            gcse.type = 'text/javascript';
            gcse.async = true;
            gcse.src = (document.location.protocol == 'https:' ? 'https:' : 'http:') +
                '//www.google.com/cse/cse.js?cx=' + cx;
            var s = document.getElementsByTagName('script')[0];
            s.parentNode.insertBefore(gcse, s);
          })();
        
  <!-- google search ends -->
  <!-- App Scripts-->

        $(document).ready(function() {
          $('#comment').hide()
            $('#form1').ajaxForm(function() {
              $('#comment').slideDown();
              $('#p1').hide();
              $('#p2').hide();
              $('#p3').hide();
              $('#p4').hide();
              $('#p5').hide();
             
              
            });
          });
        
$(document).ready(function() {
  $('#p5').hide();
            $('#form2').ajaxForm(function() {
              $('#comment').slideUp("slow");
                });
          });
function hidep()
{
  $('#comment').slideUp("slow");
              
}
function radioclick(val)
{
  document.getElementById("result").value=val;
  $('#p5').show();
}
function slider()
{
  $('#comment').slideDown();
}

$(document).ready(function()
{
  $('#results').html( '&nbsp;').load('{% url 'get_comments_A' details.id %}');
$('#opt1').tab('show')

  $('#spinner').hide();
  /* clicking A */
$('#opt1').click(function()
{
$('#results').html( '&nbsp;').load('{% url 'get_comments_A' details.id %}');
$('#opt1').tab('show')

});
 /* Clicking B */
 $('#opt2').click(function()
{
$('#results').html( '&nbsp;').load('{% url 'get_comments_B' details.id %}');
$('#opt2').tab('show')

});

$('#opt3').click(function()
{
$('#results').html( '&nbsp;').load('{% url 'get_comments_C' details.id %}');
$('#opt3').tab('show')

});

$('#opt4').click(function()
{
$('#results').html( '&nbsp;').load('{% url 'get_comments_D' details.id %}');
$('#opt4').tab('show')

});

$(document).ajaxStart(function()
{
  $('#spinner').show();
}).ajaxStop(function()
{
  $('#spinner').hide();
})
});


    