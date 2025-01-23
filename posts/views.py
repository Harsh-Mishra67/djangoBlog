from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound,HttpResponseRedirect




posts = [
    {
        "id": 1,
        "title": "Let's explore python",
        "content": "Python Is Interpreted, High level, general purpose programming language. Widely used in the fields of web development, data science and machine learning."
    },
    {
        "id": 2,
        "title": "Let's explore Javascript",
        "content": "Javascript Is Interpreted, High level, general purpose programming language. Widely used in the fields of web development."
    },
    {
        "id": 3,
        "title": "Django the best web framework",
        "content": "Django is used by almost every big tech company like Facebook, Google, YouTube, Instagram etc."
    }
]

def getAllPosts(request):
    return render(request,'all_posts.html',{'blog_posts': posts})


def individualPost(request,id):
    for post in posts:
        if(post['id']==id):
            return render(request,'individual_post.html',{'one_post':post})
    

# def home(request):
#     html=""
#     for post in posts:
#         html+=f'''
#               <div>
#                 <h1>{post['id']} - {post['title']}</h1> 
#                 <a href="/post/{post['id']}">Read More</a>
#                 <br/>
#               </div>

# '''
#     return HttpResponse(html)


# def showPage(request,id):
#     # print(type(id))
#     # return HttpResponse(f"{id} - {str(type(id))[1:-1]}")
#     # return HttpResponse(f"{id} - {(type(id))}")
#     for post in posts:
#         html=""
#         if(post['id']==id):
#             html+=f'''
#             <div>
#             <h1>{post["id"]} - {post["title"]}</h1>
#             <p>{post['content']}
#             </div>

# '''
#             return HttpResponse(html)
        

#     return HttpResponseNotFound("<p>page not found</p>")


# def redirect(request,id):
#     return HttpResponseRedirect(f'/post/{id}/')

# def realHome(request):
#     html=""
#     html+=f'''
#       <a href="/post/home">Get all the courses</a>
      
#     '''
#     return HttpResponse(html)
    



def homePage(request):
    return render(request, 'home.html')