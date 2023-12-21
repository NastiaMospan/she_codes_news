 README.md template

## About This Project
This is my first Django project. 
The idea is to have a news web site where user can create his own account, and when logged in to post a story.


## How To Run This Code
- clone the repo to your local machine,
 - create a virtual environment, 
 - migrate the database
 - Run in the terminal `python manage.py runserver`


## Database Schema
![ {{ My ERD }} ]( {{ ./users/models.png }} )

## Video link https://youtu.be/QAsaYDzLJJ4?si=yDijKf5nLymkKWg5

## Project Features

- [ ] Order stories by date. DONE
![ {{views.py: context['latest_stories'] = NewsStory.objects.order_by("-pub_date")[:4]}} ]

- [ ] Styled "new story" form. DONE
![ {{ Centered the form. Applied CSS style that matches the web title: pink-purple gradient. }} ]

- [ ] Story images. DONE.
![ {{ Updated lates news images by replacing initial placeholders. }} ]

- [ ] Log-in/log-out. DONE
![ {{ Added to the nav bar. User can log in and to log out.}} ]

- [ ] "Account view" page. DONE
![ {{ Once logged in, user can see his profile view: his email and account name}} ]

- [ ] "Create Account" DONE
![ {{ Create account is added to the nav bar. Also, when user navigate to login page, he will see the message: "Don't have an account? Create one here" }} ]

- [ ] View stories by author. DONE.
![ {{ Applies to all stories only. User can choose the author from the dropdown menu and then press submit. }} ]

- [ ] "Log-in" button only visible when no user is logged in/"Log-out" button
        only visible when a user *is* logged in.  DONE.
   

- [ ] "Create Story" functionality only available when user is logged in. DONE.
 ![ {{ Updated nav.html with  {% if user.is_authenticated %} }} ]


## Additional Features:

- [ ] Added social media share buttons. DONE.
 ![ {{ user can share the story via facebook, twitter or linkedin.}} ]

- [ ] Added comment feature. FORM FOR ADDING COMMENTS DOESNT WORK.
 ![ {{ Tested adding comment from admin site. I can see who added the comment and when, but cant see actual comment and form to add a new comment.}} ]

 -  [ ] Added "hover" feature to the links' DONE.
 ![ {{ links changing color from back to purple.}} ]


-  Add categories to the stories and allow the user to search for stories by
        category. NOT DONE
    ![ {{ Description of image }} ]( {{ ./relative_path_to_image_file }} )

-  Add the ability to update and delete stories (consider permissions - who
        should be allowed to update or and/or delete stories).NOT DONE
    ![ {{ Description of image }} ]( {{ ./relative_path_to_image_file }} )

- Add the ability to “favourite” stories and see a page with your favourite
        stories. NOT DONE
    ![ {{ Description of image }} ]( {{ ./relative_path_to_image_file }} )

-  Our form for creating stories requires you to add the publication date,
        update this to automatically save the publication date as the day the
        story was first published (maybe you could then add a field to show
        when the story was updated). NOT DONE
    ![ {{ Description of image }} ]( {{ ./relative_path_to_image_file }} )
               
-  Gracefully handle the error where someone tries to create a new story when
        they are not logged in. NOT DONE
    ![ {{ Description of image }} ]( {{ ./relative_path_to_image_file }} )
 
