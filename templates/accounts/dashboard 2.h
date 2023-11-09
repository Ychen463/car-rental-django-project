{% extends 'base.html' %}

{% block title %} | Dashboard {% endblock %}
{% block content %}
{% load static %}

<!-- Sub banner start -->
<div class="sub-banner overview-bgi">
    <div class="container breadcrumb-area">
        <div class="breadcrumb-areas">
            <h1>Dashboard</h1>
            <ul class="breadcrumbs">
                <li><a href="{% url 'home' %}">Home</a></li>
                <li class="active">{{ user.first_name }}</li>
            </ul>
        </div>
    </div>
</div>
<!-- Sub Banner end -->

<!--   Dashboard Start   -->

<div class="container mt-50 mb-50">
    {% include 'includes/messages.html' %}
	<div class="main-title" style="text-align:left !important;">
            <h1>Welcome <span>{{ user.first_name }}</span></h1>
            <p>Here are the cars that you have inquired about</p>
		</div>
	{% if inquires %}
	
	<table class="table table-hover">
	  <thead>
		<tr>
		  <th scope="col">S.No</th>
		  <th scope="col">Car Name</th>
		  <th scope="col">Location</th>
		  <th scope="col">Action</th>
		</tr>
	  </thead>
	  <tbody>
		{% for inquiry in inquires %}
		<tr>
		  <!-- <th scope="row">{{ forloop.counter }}</th> -->
		  <th scope="row">1</th>
		  <td>{{inquiry.car_title}}</td>
		  <td>{{inquiry.city}}</td>
		  <td><a href="{% url 'car_detail' inquiry.car_id %}" class="btn btn-outline-dark">View Car</a></td>
		</tr>
		{% endfor %}
	  </tbody>
	</table>
	{% else %}
		<h4>You have no inquiries</h4>
	{% endif %}
</div>

<!--   Dashboard End   -->

{% endblock %}