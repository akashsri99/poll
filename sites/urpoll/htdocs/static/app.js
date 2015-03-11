
 $(window).load(function() {
    $('#loading').hide();
  });

  (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
  (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
  m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
  })(window,document,'script','//www.google-analytics.com/analytics.js','ga');

  ga('create', 'UA-60074856-1', 'auto');
  ga('send', 'pageview');

     function statusChangeCallback(response,val) {
    console.log('statusChangeCallback');
    console.log(response);
    if (response.status === 'connected') {
      if(val===1){
          $('#p5').show(); //for radio button
 }
 } else if (response.status === 'not_authorized') {
      if(val===1) //radio button click
      {
        $('#p5').hide();
      }
      else if (val==2) //disabling the comment box
      {
        $('#pcomment').hide();
      }
      else if (val===3) 
        {
          $('#sques').hide(); //disabling from posting a question
        };
       document.getElementById('status').innerHTML = 'Please log ' +
        'into this app.';
    } 
else {
     if(val===1) //radio button click
      {
        $('#p5').hide();
      }
      else if (val==2) //disabling the comment box
      {
        $('#pcomment').hide();
      }
      else if (val===3) 
        {
          $('#sques').hide(); //disabling from posting a question
        };
      document.getElementById('status').innerHTML = 'Please log ' +
        'into Facebook.';
    }
  }

  function checkUser(val)
  {
   checkLoginState(val);

  }
  function checkLoginState(val) {
    FB.getLoginStatus(function(response) {
      statusChangeCallback(response,val);
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
 
  function testAPI() {
    console.log('Welcome!  Fetching your information.... ');
    FB.api('/me', function(response) {
      console.log('Successful login for: ' + response.name);
      document.getElementById('status').innerHTML =response.id ;
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




    