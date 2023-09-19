from django.shortcuts import render

# Sample data for detailed views
sample_data = {
    1: "Detail for item 1",
    2: "Detail for item 2",
    3: "Detail for item 3",
}

def index(request):
    # Render the main HTML page
    return render(request, 'index.html', {'data': sample_data})

def detail(request, item_id):
    # Render a detailed view for the specified item
    item_detail = sample_data.get(item_id, "Item not found")
    return render(request, 'detail.html', {'item_detail': item_detail})

