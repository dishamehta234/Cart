#!/usr/bin/env python
#-*- coding: UTF-8 -*-

from werkzeug.utils import escape
from werkzeug.wrappers import Request, Response

@Request.application
def Cart(request):
   showdata = ['<title>Cart Details</title>']
 
   showdata.append('''
    <html>
       <head>
       <script language="javascript">
            
        function orange(){
            var orangequanti = document.getElementById('Q1').value;
            if(orangequanti==0)
            {
              document.getElementById('error').innerHTML="Please Enter Quantity";
            }
            else
            {
             var orgtot=orangequanti*150;
            document.getElementById('qua1').innerHTML= "oranges ->   " + orangequanti +"  *150  =" + orgtot+ "<input type='button' id='remove1' value='Remove' onclick='removeOrange()'><br><br>";
            }
          }
          function removeOrange(){
              document.getElementById('Q1').value="";
              document.getElementById('qua1').innerHTML="";
          }
          function apple(){
            var applequanti = document.getElementById('Q2').value;
            if(applequanti==0)
            {
              document.getElementById('error1').innerHTML="Please Enter Quantity";
            }
            else
            {
             var apptot=applequanti*200 ;
              document.getElementById('qua2').innerHTML= "Apple ->   " + applequanti +"  *200  =" +apptot + "<input type='button' id='remove2' value='Remove' onclick='removeApple()'><br><br>";
            }   
          }
          function removeApple(){
              document.getElementById('Q2').value="";
              document.getElementById('qua2').innerHTML="";
          }
          function grapes(){
            var grapesquanti = document.getElementById('Q3').value;
            if(grapesquanti==0)
            {
              document.getElementById('error2').innerHTML="Please Enter Quantity";
            }
            else
            {
              var graptotl=grapesquanti*70;
              document.getElementById('qua3').innerHTML= "Grapes ->   " + grapesquanti +"  *70  =" + graptotl+ "<input type='button' id='remove3' value='Remove' onclick='removeGrapes()'><br><br>";
            }   
          }
          function removeGrapes(){
              document.getElementById('Q3').value="";
              document.getElementById('qua3').innerHTML="";
          }
        </script>
        </head>
        <body bgcolor="skyblue">
       <table>
       <tr>
        <td>
                  <img src="orange.jpg" alt="Oranges" height="50px" width="50px"/>
                  <h3>Orange<br>150 Rs/Kg</h3>
                  <input type="text" placeholder="Quantity" id="Q1">
                  <input type="submit" value="Add to Cart" onclick="orange()">
                  <span id="error"></span>
             </td>
        <td align="right"><i id="qua1"></i></td>
        </tr>
        <tr>
        <td>
                  <img src="Apple.jpg" alt="Apples" height="50px" width="50px" />
                  <h3>Apple<br>200 Rs/Kg</h3>
                  <input type="text" placeholder="Quantity" id="Q2">
                  <input type="submit" value="Add to Cart" onclick="apple()">     
                  <span id="error1"></span>
             </td>
             <td align="right"><i id="qua2"></i></td>
        </tr>
         <tr>
        <td>
                  <img src="grapes.jpg" alt="Grapes" height="50px" width="50px" />
                  <h3>Grapes<br>70 Rs/Kg</h3>
                  <input type="text" placeholder="Quantity" id="Q3">
                  <input type="submit" value="Add to Cart" onclick="grapes()">                  
                  <span id="error2"></span>
             </td>
            <td align="right"><i id="qua3"></i></td>
        </tr>
        </table>
       </body>
      </html>
    ''')
   return Response(''.join(showdata), mimetype='text/html')
   
   from werkzeug.serving import run_simple
   run_simple('localhost', 4000, Cart)
