+ define route correctly
    + what do you mean by "this" route?
    + login page, is a route?
    + handle upload
+ i want a image uploader system

+ what do i want?
    + gallery
        + general gallery
        + private gallery
            + user account system
                + delete option
        + download photo

+ according to the above requirements, describe a URL scheme for your app
=========================================================================

+ shimages.com: 
    + upload thing
    + login
    + register
    + Explore (general gallery)

+ upload thing (without login)
    + shimages.com/anonymous/1
        + Image
        + Link
        + View in gallery
        + Download 

+ View in gallery (without login)
    + shimages.com/explore or shimages.com/explore/anonymous
        + thumbnails of uploads without login
+ Login
   + shimages.com 
        + Indicate that logged in

+ Upload thing (with login)
    + shimages.com/<username>/23
        + disable <username> called 'anonymous'
        + Image
        + Link
        + Download
        + Delete
        + View in gallery

+ View in gallery (with login)
    + shimages.com/explore/<username>

================================================

public routes
--------------

shimages.com
shimages.com/uploaded
shimages.com/uploaded/n

shimages.com/<username>/uploaded
shimages.com/<username>/uploaded/n

shimages.com/static/images/[obfuscated_name].[jpg|png|...]

shimages.com/<username>/settings

shimages.com/register
shimages.com/register_confirmed

private routes
--------------
