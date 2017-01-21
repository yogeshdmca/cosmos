# import json
# from django.http import HttpResponse
# from django.shortcuts import render
# from profile.models import UserInfo, FlatNumber

# def ajax_search_by(request):
# 	ctx = {}
# 	search_name = request.POST['search_name']
# 	if search_name == 'Flat Number':
# 		flat_numbers = FlatNumber.objects.all()
# 		for flats in flat_numbers:
# 			ctx[flats.id] = flats.block
# 	else:
# 		users = UserInfo.objects.all()
# 		if search_name == 'Serial Number':
# 			for obj in users:
# 				ctx[obj.id] = obj.serial_number
# 		if search_name == 'Vehicle Number':
# 			for obj in users:
# 				ctx[obj.id] = obj.vehicle_number
# 	return HttpResponse(json.dumps(ctx),status = 200)
