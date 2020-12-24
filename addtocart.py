#!/usr/bin/env python
#-*- coding: UTF-8 -*-

from werkzeug.utils import escape
from werkzeug.wrappers import Request, Response

@Request.application
def Cart(request):
   showdata = ['<title>Cart Details</title>']
 
   showdata.append('''
       <script language="JavaScript">
           function showInput() {
                   document.getElementById('display').innerHTML =
                   document.getElementByName("h1");
           }
       </script>
       <div id="header">
       		<h1>
       			Product Details
       			<i align="right"><input type="text" id="searchdata" size="20" placeholder="Serach Product"/></i>
       		</h1>       				
       </div>
       <div id="mainprodutcs">
       	<div id="productline1">
       		<table>
	       		<tr>
	       		<td>
		       		<div id="product1" padding="5px">
		       			<img src="../Pictures/orange.jpg" alt="Orange" height="50px" width="50px"  align="center"/>
		       			<h1>Oranges</h1>
		       			<h3>Price : 60 Rs/Kg</h3>
		       			<i> <input type="submit" name="product1" value="Add To Cart"> </i>
		       		</div>
		       	</td>
		       	<td>
		       		<div id="product2">
		       		    <img  src="../Pictures/orange.jpg" alt="Apple" height="50px" width="50px" src="" align="center"/>
		       			<h1>Apple</h1>
		       			<h3>Price : 80 Rs/Kg</h3>
		       			<i> <input type="submit" name="product2" value="Add To Cart"> </i>
		       		</div>
		       	</td>
		       	<td>
		       		<div id="product3">
		       		    <img  src="../Pictures/orange.jpg" alt="Apple" height="50px" width="50px" src="" align="center"/>
		       			<h1>Grapes</h1>
		       			<h3>Price : 180 Rs/Kg</h3>
		       			<i> <input type="submit" name="product3" value="Add To Cart"> </i>
		       		</div>
		       	</td>
	       		</tr>
	       		<tr>
	       		<td>
		       		<div id="product4" padding="5px">
		       			<img src="../Pictures/orange.jpg" alt="Strawbery" height="50px" width="50px"  align="center"/>
		       			<h1>Strawbery</h1>
		       			<h3>Price : 160 Rs/Kg</h3>
		       			<i> <input type="submit" name="product4" value="Add To Cart"> </i>
		       		</div>
		       	</td>
		       	<td>
		       		<div id="product5">
		       		    <img  src="../Pictures/orange.jpg" alt="GreenApple" height="50px" width="50px" src="" align="center"/>
		       			<h1>Apple</h1>
		       			<h3>Price : 80 Rs/Kg</h3>
		       			<i> <input type="submit" name="product2" value="Add To Cart"> </i>
		       		</div>
		       	</td>
		       	<td>
		       		<div id="product6">
		       		    <img  src="../Pictures/orange.jpg" alt="Banana" height="50px" width="50px" src="" align="center"/>
		       			<h1>Grapes</h1>
		       			<h3>Price : 180 Rs/Kg</h3>
		       			<i> <input type="submit" name="product6" value="Add To Cart"> </i>
		       		</div>
		       	</td>
	       		</tr>
       		</table>
       	</div>
       </div>

      
   ''')
   return Response(''.join(showdata), mimetype='text/html')
if __name__ == '__main__':
   from werkzeug.serving import run_simple
   run_simple('localhost',4000, Cart)