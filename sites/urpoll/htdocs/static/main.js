<script language="javascript">
<script src="http://ajax.googleapis.com/ajax/libs/jquery/1.11.2/jquery.min.js"></script>
<script src="http://ajax.googleapis.com/ajax/libs/jquery/1.7/jquery.js"></script> 
<script src="http://malsup.github.com/jquery.form.js"></script> 
<script>  
        $(document).ready(function() {

            $('#form').ajaxForm(function() {

              $('#prblm1').hide();
              $('#prblm2').hide();
              $('#prblm3').hide();
              $('#prblm4').hide();
              $('#prblm5').hide();
              $('#panel').slideDown("slow");
                });
          });

              


       </script> 
 

<script>
function radioclick(val)
{
  document.getElementById("result").value=val;
  if(val==1)
  {
    $("#test1").html("Why  A  ? ");
  }
  if(val==2)
  {
    $("#test1").html("Why  B  ? ");
  }
  if(val==3)
  {
    $("#test1").html("Why  C  ? ");
  }
  if(val==4)
  {
    $("#test1").html("Why D ? ");
  }
}

 $(document).ready(function() {

            $('#form2').ajaxForm(function() {
              $('#panel').slideUp("slow");
                });
          });


</script>

<script>
$(document).ready(function()
{
  $('#spinner').hide();
  /* clicking A */
$('#opt1').click(function()
{
$('#results').html( '&nbsp;').load('{% url 'get_comments_A' details.id %}');
});
 /* Clicking B */
 $('#opt2').click(function()
{
$('#results').html( '&nbsp;').load('{% url 'get_comments_B' details.id %}');
});

$('#opt3').click(function()
{
$('#results').html( '&nbsp;').load('{% url 'get_comments_C' details.id %}');
});

$('#opt4').click(function()
{
$('#results').html( '&nbsp;').load('{% url 'get_comments_D' details.id %}');
});

$(document).ajaxStart(function()
{
  $('#spinner').show();
}).ajaxStop(function()
{
  $('#spinner').hide();
})
});
</script>
</script>
