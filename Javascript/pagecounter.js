// Visit https://countapi.xyz/ to View Documentation and Create your API

# html
<div id="counter">
<span id="pageviews">Pageviews: </span><span id="count">0</span>
</div>


# css
#counter {
font-size: 24px;
font-family: Arial, sans-serif;
}
#pageviews {
color: lightgrey;
}
#count {
font-weight: bold;
color: pink;
}


# Javascript
const countEl = document.getElementById('count');

updateVisitCount();

function updateVisitCount() {
	fetch('https://api.countapi.xyz/update/YOUR_URL/count/?amount=1')
	.then(res => res.json())
	.then(res => {
		countEl.innerHTML = res.value;
	})
}
