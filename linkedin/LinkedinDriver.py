from bs4 import BeautifulSoup
import requests

# Load the HTML content (assuming it is saved as a file or you paste it as a string)
html_content = """<div class="pv-recent-activity-detail__core-rail">
        <section class="artdeco-card pb3">
<!---->
  
            <h2 class="text-heading-large ph5 pt5 pb2">
              All activity
            </h2>
            
          
  
    
    <div class="mb3">
      
        
      <div class="pv2 ph5">
        <div class="display-flex white-space-nowrap" role="group" aria-label="Select type of recent activity">
            
  <button aria-pressed="false" tabindex="-1" class="profile-creator-shared-pills__pill artdeco-pill artdeco-pill--slate artdeco-pill--choice artdeco-pill--3 artdeco-pill--toggle
      " id="content-collection-pill-0" type="button">
    <span class="artdeco-pill__text">Posts</span>
<!---->  </button>

            
  <button aria-pressed="true" tabindex="0" class="profile-creator-shared-pills__pill artdeco-pill artdeco-pill--slate artdeco-pill--choice artdeco-pill--3 artdeco-pill--toggle
      artdeco-pill--selected" id="content-collection-pill-1" type="button">
    <span class="artdeco-pill__text">Comments</span>
<!---->  </button>

            
  <button aria-pressed="false" tabindex="-1" class="profile-creator-shared-pills__pill artdeco-pill artdeco-pill--slate artdeco-pill--choice artdeco-pill--3 artdeco-pill--toggle
      " id="content-collection-pill-2" type="button">
    <span class="artdeco-pill__text">Reactions</span>
<!---->  </button>

<!---->        </div>
      </div>
  
      
    </div>
    <div class="pv0 ph5">
      
          
      <div>
        
              
    <div class="scaffold-finite-scroll
    scaffold-finite-scroll--infinite
     full-width">
  <!---->
  
      <div class="scaffold-finite-scroll__content">
        
        <div class="visually-hidden" aria-live="polite">
          Loaded 94 Comments posts
        </div>

          <ul class="display-flex flex-wrap list-style-none justify-center">
                <li class="profile-creator-shared-feed-update__container">
                  <div>
  
                        
    <div class="relative">
      <div class="profile-creator-shared-feed-update__anchor"></div>
      
      
        
        
          
    <div class="full-height" data-view-name="feed-full-update">
      <div class="full-height">
        <div class="feed-shared-update-v2 feed-shared-update-v2--minimal-padding full-height relative
            
            feed-shared-update-v2--e2e
            
            
            
            artdeco-card
            
            
            
            " id="ember1777" role="region" data-urn="urn:li:activity:7242285086220460033">
          
      <div>
        
            <div role="status">
<!---->            </div>
              <div class="display-flex flex-column flex-grow-1">
                
                <h2 class="visually-hidden">
                    Feed post number 1
                </h2>
                <div id="fie-impression-container">
<!---->                  <div class="relative">
                      
    <div class="update-components-header
        update-components-header--with-control-menu
        update-components-header--with-divider
        update-components-header--with-image
        t-12 t-black--light t-normal pt2
        ">
      <div class="update-components-header__text-wrapper
          ">
<!---->            <a class="app-aware-link " data-control-id="kwtcRMmzUhctpiJOhD0IJQ==" target="_self" href="https://www.linkedin.com/in/pabloborda?miniProfileUrn=urn%3Ali%3Afsd_profile%3AACoAAAJy9kYBOWygCujiqHyQHvPOsfBSqkXuhcc" data-test-app-aware-link="">
              
    <div class="ivm-image-view-model    update-components-header__image mr2">
        
    <div class="ivm-view-attr__img-wrapper
        
        ">
<!---->
<!---->          <img width="24" src="https://media.licdn.com/dms/image/v2/D4E35AQGpp9o3t9TbVw/profile-framedphoto-shrink_100_100/profile-framedphoto-shrink_100_100/0/1724455776612?e=1727359200&amp;v=beta&amp;t=Jy5folMOCojzWpT-TRK_XET0XnlVlghrs2L_a6_tfyo" loading="lazy" height="24" alt="Pablo Tomas’ profile photo" id="ember1778" class="ivm-view-attr__img--centered EntityPhoto-circle-0   evi-image lazy-image ember-view">
    </div>
  
          </div>
  
            </a>
          <span class="update-components-header__text-view">
            <span><a href="/in/pabloborda/" id="ember1779" class="ember-view"><!---->Pablo Tomas Borda<!----></a></span><span class="white-space-pre"> </span>commented on this<!---->
          </span>
      </div>
<!---->    </div>
  
                      
    <div class="feed-shared-control-menu display-flex
        feed-shared-update-v2__control-menu absolute text-align-right
        
        ">
<!---->
        <div id="ember1781" class="artdeco-dropdown artdeco-dropdown--placement-bottom artdeco-dropdown--justification-right ember-view">
          <button aria-expanded="false" aria-label="Open control menu for post by Nihad Kerić" tabindex="0" id="ember1782" class="feed-shared-control-menu__trigger artdeco-button artdeco-button--tertiary artdeco-button--muted artdeco-button--1 artdeco-button--circle artdeco-dropdown__trigger artdeco-dropdown__trigger--placement-bottom ember-view" type="button">
                <svg role="none" aria-hidden="true" class="artdeco-button__icon" xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16" data-supported-dps="16x16" data-test-icon="overflow-web-ios-small">
<!---->    
    <use href="#overflow-web-ios-small" width="16" height="16"></use>
</svg>

                      
<!----></button>
          <div tabindex="-1" aria-hidden="true" id="ember1783" class="feed-shared-control-menu__content artdeco-dropdown__content artdeco-dropdown--is-dropdown-element artdeco-dropdown__content--has-arrow artdeco-dropdown__content--arrow-right artdeco-dropdown__content--justification-right artdeco-dropdown__content--placement-bottom ember-view" aria-label="Control Menu Options"><!----></div>
        </div>

<!---->
<!---->
<!---->
<!---->
<!---->
<!----><!---->    </div>
  
<!----><!---->                      
    <div class="update-components-actor display-flex
        
        
        
        
        ">
<!---->
      <div class="update-components-actor__container
          
          display-flex flex-grow-1">
          <a class="app-aware-link  update-components-actor__image relative" aria-label="Nihad Kerić, graphic." target="_self" href="https://www.linkedin.com/in/nihkrc?miniProfileUrn=urn%3Ali%3Afsd_profile%3AACoAABZJHh8Bk0o3zoApIdYX0bAMuVRdLFu6BCQ" data-test-app-aware-link="">
            <span class="js-update-components-actor__avatar">
              
    <div class="ivm-image-view-model    update-components-actor__avatar">
        
    <div class="ivm-view-attr__img-wrapper
        
        ">
<!---->
<!---->          <img width="48" src="https://media.licdn.com/dms/image/v2/C4D03AQHcPAZfDBDqXw/profile-displayphoto-shrink_100_100/profile-displayphoto-shrink_100_100/0/1560778197631?e=1732147200&amp;v=beta&amp;t=AlCq_t-5mfJtzgliujNOHdcDLcUupsQVndmOf3XsxO8" loading="lazy" height="48" alt="" id="ember1784" class="ivm-view-attr__img--centered EntityPhoto-circle-3  update-components-actor__avatar-image evi-image lazy-image ember-view">
    </div>
  
          </div>
  
            </span>
          </a>
        <div class="update-components-actor__meta relative
            ">
          <a class="app-aware-link  update-components-actor__meta-link" aria-label="View: Nihad Kerić • 3rd+ Software Engineer | Frontend | UI/UX | Responsive Design | API Integration | Software Architecture | Digital Transformation" target="_self" href="https://www.linkedin.com/in/nihkrc?miniProfileUrn=urn%3Ali%3Afsd_profile%3AACoAABZJHh8Bk0o3zoApIdYX0bAMuVRdLFu6BCQ" data-test-app-aware-link="">
            <span class="update-components-actor__title
                ">
              <span class="update-components-actor__name hoverable-link-text t-14 t-bold
                  
                  t-black">
                  <span dir="ltr"><span aria-hidden="true"><!---->Nihad Kerić<!----></span><span class="visually-hidden"><!---->Nihad Kerić<!----></span></span>
              </span>
                <span class="update-components-actor__supplementary-actor-info
                    t-black--light
                    t-14 t-normal
                    
                    ">
                    <span aria-hidden="true"><span class="white-space-pre"> </span>• 3rd+<!----></span><span class="visually-hidden"><span class="white-space-pre"> </span>• 3rd+<!----></span>
                </span>
            </span>

              <span class="update-components-actor__description
                  t-black--light
                  
                  t-12 t-normal
                  ">
                  <span aria-hidden="true"><!---->Software Engineer | Frontend | UI/UX | Responsive Design | API Integration | Software Architecture | Digital Transformation<!----></span><span class="visually-hidden"><!---->Software Engineer | Frontend | UI/UX | Responsive Design | API Integration | Software Architecture | Digital Transformation<!----></span>
              </span>

          </a>
<!---->              <a class="app-aware-link  update-components-actor__sub-description-link" aria-label="2 days ago" target="_self" href="https://www.linkedin.com/in/nihkrc?miniProfileUrn=urn%3Ali%3Afsd_profile%3AACoAABZJHh8Bk0o3zoApIdYX0bAMuVRdLFu6BCQ" data-test-app-aware-link="">
                <span class="update-components-actor__sub-description t-12 t-normal
                    t-black--light
                    
                    ">
                    <span aria-hidden="true"><!---->2d •<span class="white-space-pre"> </span><span><li-icon aria-hidden="true" type="globe-americas" class="v-align-bottom" size="small"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16" data-supported-dps="16x16" fill="currentColor" class="mercado-match" width="16" height="16" focusable="false">
      <path d="M8 1a7 7 0 107 7 7 7 0 00-7-7zM3 8a5 5 0 011-3l.55.55A1.5 1.5 0 015 6.62v1.07a.75.75 0 00.22.53l.56.56a.75.75 0 00.53.22H7v.69a.75.75 0 00.22.53l.56.56a.75.75 0 01.22.53V13a5 5 0 01-5-5zm6.24 4.83l2-2.46a.75.75 0 00.09-.8l-.58-1.16A.76.76 0 0010 8H7v-.19a.51.51 0 01.28-.45l.38-.19a.74.74 0 01.68 0L9 7.5l.38-.7a1 1 0 00.12-.48v-.85a.78.78 0 01.21-.53l1.07-1.09a5 5 0 01-1.54 9z"></path>
    </svg></li-icon></span><span class="white-space-pre"> </span><!----><!----></span><span class="visually-hidden"><!---->2 days ago<!----></span>
                </span>
              </a>
        </div>
      </div>

        
    <button class="follow   update-components-actor__follow-button update-components-update-v2__follow-button artdeco-button
            
            
            artdeco-button--tertiary
            
            
            " aria-label="Follow Nihad Kerić" type="button">
          <svg role="none" aria-hidden="true" class="artdeco-button__icon" xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16" data-supported-dps="16x16" data-test-icon="add-small">
<!---->    
    <use href="#add-small" width="16" height="16"></use>
</svg>

        <span aria-hidden="true">Follow</span>
    </button>
  

<!---->    </div>
  
                  </div>
<!---->
                  <!---->

<!----><!---->                          
    <div class="feed-shared-update-v2__description-wrapper  mr2" style="" tabindex="-1">
          
    <div class="feed-shared-inline-show-more-text
        feed-shared-update-v2__description feed-shared-inline-show-more-text--minimal-padding
        
        feed-shared-inline-show-more-text--3-lines
        
        
        
        " tabindex="-1">
      
            
    <div class="update-components-text relative update-components-update-v2__commentary " dir="ltr">
<!---->
      <span class="break-words
          tvm-parent-container">
<!---->          <span dir="ltr"><!---->💡 Bye Bye Try/Catch, Meet New ECMAScript Operator 💡<!----><span><br></span><span><br></span><!---->Benefits of using ?= operator instead of try/catch:<!----><span><br></span><span><br></span><!---->✅ Simplified Error Handling: Streamline error management by eliminating the need for try-catch blocks.<!----><span><br></span><!---->✅ Enhanced Readability: Improve code clarity by reducing nesting and making error handling flow more intuitive.<!----><span><br></span><!---->✅ Consistency Across APIs: Establish a uniform approach to error handling across various APIs, ensuring predictable behavior.<!----><span><br></span><!---->✅ Improved Security: Reduce the risk of overlooking error handling, thereby enhancing the overall security of the code.<!----><span><br></span><span><br></span><a class="app-aware-link " href="https://www.linkedin.com/feed/hashtag/?keywords=javascript&amp;highlightedUpdateUrns=urn%3Ali%3Aactivity%3A7241680825530896384" data-test-app-aware-link=""><span class="visually-hidden">hashtag</span><span><span aria-hidden="true">#</span>javascript</span></a><span class="white-space-pre"> </span><!----><!----><a class="app-aware-link " href="https://www.linkedin.com/feed/hashtag/?keywords=javascriptdeveloper&amp;highlightedUpdateUrns=urn%3Ali%3Aactivity%3A7241680825530896384" data-test-app-aware-link=""><span class="visually-hidden">hashtag</span><span><span aria-hidden="true">#</span>javascriptdeveloper</span></a><span class="white-space-pre"> </span><!----><!----><a class="app-aware-link " href="https://www.linkedin.com/feed/hashtag/?keywords=frontend&amp;highlightedUpdateUrns=urn%3Ali%3Aactivity%3A7241680825530896384" data-test-app-aware-link=""><span class="visually-hidden">hashtag</span><span><span aria-hidden="true">#</span>frontend</span></a><span class="white-space-pre"> </span><!----><!----><a class="app-aware-link " href="https://www.linkedin.com/feed/hashtag/?keywords=softwareengineer&amp;highlightedUpdateUrns=urn%3Ali%3Aactivity%3A7241680825530896384" data-test-app-aware-link=""><span class="visually-hidden">hashtag</span><span><span aria-hidden="true">#</span>softwareengineer</span></a><span class="white-space-pre"> </span><!----><!----><a class="app-aware-link " href="https://www.linkedin.com/feed/hashtag/?keywords=frontendengineer&amp;highlightedUpdateUrns=urn%3Ali%3Aactivity%3A7241680825530896384" data-test-app-aware-link=""><span class="visually-hidden">hashtag</span><span><span aria-hidden="true">#</span>frontendengineer</span></a><span class="white-space-pre"> </span><!----><!----><a class="app-aware-link " href="https://www.linkedin.com/feed/hashtag/?keywords=web&amp;highlightedUpdateUrns=urn%3Ali%3Aactivity%3A7241680825530896384" data-test-app-aware-link=""><span class="visually-hidden">hashtag</span><span><span aria-hidden="true">#</span>web</span></a><span class="white-space-pre"> </span><!----><!----><a class="app-aware-link " href="https://www.linkedin.com/feed/hashtag/?keywords=webdeveloper&amp;highlightedUpdateUrns=urn%3Ali%3Aactivity%3A7241680825530896384" data-test-app-aware-link=""><span class="visually-hidden">hashtag</span><span><span aria-hidden="true">#</span>webdeveloper</span></a></span>
      </span>
    </div>
  
          <button role="button" class="feed-shared-inline-show-more-text__see-more-less-toggle see-more t-14 t-black--light t-normal hoverable-link-text feed-shared-inline-show-more-text__dynamic-more-text
            feed-shared-inline-show-more-text__dynamic-bidi-text" aria-label="see more, visually reveals content which is already detected by screen readers" style="left:314.734375px" type="button">
          <span>…more</span>
        </button><!---->    </div>
  
        
<!---->    </div>
  
                          
    <div class="update-components-image
        update-components-image--single-image
        feed-shared-update-v2__content">
      <div class="relative">
        <div class="update-components-image__container
            " style="
        padding-top: 85.7%;">
<!---->
                <button class="update-components-image__image-link" type="button">
                    <span class="visually-hidden">
                      Activate to view larger image,
                    </span>
                  
    <div class="ivm-image-view-model   ">
        
    <div class="ivm-view-attr__img-wrapper
        
        ">
<!---->
<!---->          <img width="600" src="https://media.licdn.com/dms/image/v2/D4D22AQHPkntAfijdmA/feedshare-shrink_800/feedshare-shrink_800/0/1726551250559?e=1729728000&amp;v=beta&amp;t=SxyqYvvkfdealT_FZVRZw1edqMg75kUpnryJuOl4DAo" loading="lazy" height="514" alt="Image preview" id="ember1786" class="ivm-view-attr__img--centered ivm-view-attr__img--aspect-fill update-components-image__image evi-image lazy-image ember-view">
    </div>
  
          </div>
  
                </button>
<!---->              <!---->        </div>
        <span class="visually-hidden" id="update-components-image-ember1785" aria-hidden="true">
              Activate to view larger image,
        </span>

<!---->
<!---->      </div>

<!---->
<!---->    </div>
  
<!---->
<!---->
                      <!---->
                      <!---->

                  <!---->

                    
    <div>
        
<!---->      
    <div class="display-flex align-items-center">
        <button aria-label="Scroll left" id="ember7639" class="artdeco-button artdeco-button--muted artdeco-button--1 artdeco-button--tertiary ember-view coach-shared-hscroll-bar__left-button">        <svg role="none" aria-hidden="true" class="artdeco-button__icon " xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16" data-supported-dps="16x16" data-test-icon="chevron-left-small" data-rtl="true">
<!---->    
    <use href="#chevron-left-small" width="16" height="16"></use>
</svg>


<span class="artdeco-button__text">
    
</span></button>

      <ul class="AyRYmMSzOagyjSNpOpeoYsYthQRatAhPAQ
          ">
          <li class="BMQwZPFfZNhnQoxwlNxubnHOxZAOSeE
              sxIHQIyvSardvmGfAmmHyMgaEShFEJpLLME
              ">
            
        
    
          
    <button aria-label="What impact does ECMAScript have on JavaScript development?" id="ember1787" class="artdeco-button artdeco-button--muted artdeco-button--2 artdeco-button--secondary ember-view idLvzjapkktFjkrQZrmyYDdosJLqbmSaVzEQ feed-shared-coach-prompt__multi-suggestion-cta
              feed-shared-coach-prompt__multi-suggestion-cta--first">        <svg role="none" aria-hidden="true" class="artdeco-button__icon " xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16" data-supported-dps="16x16" data-test-icon="signal-ai-small">
<!---->    
    <use href="#signal-ai-small" width="16" height="16"></use>
</svg>


<span class="artdeco-button__text">
    What impact does ECMAScript have on JavaScript development?
</span></button>
  
        
  
      
          </li>
          <li class="BMQwZPFfZNhnQoxwlNxubnHOxZAOSeE
              
              ">
            
        
    
          
    <button aria-label="What is the importance of error handling in software development?" id="ember1788" class="artdeco-button artdeco-button--muted artdeco-button--2 artdeco-button--secondary ember-view idLvzjapkktFjkrQZrmyYDdosJLqbmSaVzEQ feed-shared-coach-prompt__multi-suggestion-cta
              ">        <svg role="none" aria-hidden="true" class="artdeco-button__icon " xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16" data-supported-dps="16x16" data-test-icon="signal-ai-small">
<!---->    
    <use href="#signal-ai-small" width="16" height="16"></use>
</svg>


<span class="artdeco-button__text">
    What is the importance of error handling in software development?
</span></button>
  
        
  
      
          </li>
          <li class="BMQwZPFfZNhnQoxwlNxubnHOxZAOSeE
              
              heDDUbTxngdPzddXJBRgfzCMFhPHbtcCYk">
            
        
    
          
    <button aria-label="How does JavaScript benefit from using the ?= operator?" id="ember1789" class="artdeco-button artdeco-button--muted artdeco-button--2 artdeco-button--secondary ember-view idLvzjapkktFjkrQZrmyYDdosJLqbmSaVzEQ feed-shared-coach-prompt__multi-suggestion-cta
              ">        <svg role="none" aria-hidden="true" class="artdeco-button__icon " xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16" data-supported-dps="16x16" data-test-icon="signal-ai-small">
<!---->    
    <use href="#signal-ai-small" width="16" height="16"></use>
</svg>


<span class="artdeco-button__text">
    How does JavaScript benefit from using the ?= operator?
</span></button>
  
        
  
      
          </li>
      </ul>

        <button aria-label="Scroll right" id="ember2122" class="artdeco-button artdeco-button--muted artdeco-button--1 artdeco-button--tertiary ember-view coach-shared-hscroll-bar__right-button">        <svg role="none" aria-hidden="true" class="artdeco-button__icon " xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16" data-supported-dps="16x16" data-test-icon="chevron-right-small" data-rtl="true">
<!---->    
    <use href="#chevron-right-small" width="16" height="16"></use>
</svg>


<span class="artdeco-button__text">
    
</span></button>
    </div>
  
  
    </div>
  

                      
    
    <div id="ember1790" class="update-v2-social-activity
        
        
        ">
      
          
    <div class="social-details-social-counts
        
        
        
        
        ">
      <div class="display-flex flex-grow-1
          ">
        <div class="relative full-width">
          <ul class="display-flex
              ">
              <li class="social-details-social-counts__item social-details-social-counts__reactions
                  social-details-social-counts__reactions--left-aligned
                  
                  ">
                <button aria-label="2,948 reactions" class="t-black--light display-flex align-items-center social-details-social-counts__count-value social-details-social-counts__count-value-hover
                    t-12
                    hoverable-link-text
                    " type="button">
    <img class="reactions-icon social-detail-social-counts__count-icon social-detail-social-counts__count-icon--0 reactions-icon__consumption--small data-test-reactions-icon-type-LIKE data-test-reactions-icon-theme-light" src="https://static.licdn.com/aero-v1/sc/h/8ekq8gho1ruaf8i7f86vd1ftt" alt="like" data-test-reactions-icon-type="LIKE" data-test-reactions-icon-theme="light">
  
    <img class="reactions-icon social-detail-social-counts__count-icon social-detail-social-counts__count-icon--1 reactions-icon__consumption--small reactions-icon--stacked data-test-reactions-icon-type-INTEREST data-test-reactions-icon-theme-light" src="https://static.licdn.com/aero-v1/sc/h/lhxmwiwoag9qepsh4nc28zus" alt="insightful" data-test-reactions-icon-type="INTEREST" data-test-reactions-icon-theme="light">
  
    <img class="reactions-icon social-detail-social-counts__count-icon social-detail-social-counts__count-icon--2 reactions-icon__consumption--small reactions-icon--stacked data-test-reactions-icon-type-EMPATHY data-test-reactions-icon-theme-light" src="https://static.licdn.com/aero-v1/sc/h/cpho5fghnpme8epox8rdcds22" alt="love" data-test-reactions-icon-type="EMPATHY" data-test-reactions-icon-theme="light">
                      <span aria-hidden="true" class="social-details-social-counts__reactions-count">
2,948                    </span>
                </button>
              </li>

                <li class="social-details-social-counts__item social-details-social-counts__comments
                    social-details-social-counts__item--right-aligned
                    ">
                    <button aria-label="221 comments" class="t-black--light social-details-social-counts__count-value social-details-social-counts__count-value-hover
                        t-12
                        hoverable-link-text social-details-social-counts__link
                        " type="button">
                      <span aria-hidden="true">
                          221 comments
                      </span>
                    </button>
                </li>

                <li class="social-details-social-counts__item
                    social-details-social-counts__item--right-aligned
                    ">
                    <button id="ember1791" class="ember-view t-black--light social-details-social-counts__count-value-hover
                        t-12
                        hoverable-link-text social-details-social-counts__link" aria-label="305 reposts">
                      <span aria-hidden="true">
                        305 reposts
                      </span>
                    </button>
                </li>

<!---->          </ul>
        </div>
      </div>
    </div>
  

<!---->
<!---->
          
    <div class="feed-shared-social-action-bar
        
        feed-shared-social-action-bar--full-width
        feed-shared-social-action-bar--has-identity-toggle
        feed-shared-social-action-bar--has-social-counts">
      
              
    <div class="feed-shared-social-action-bar__action-button">
      <button aria-label="Open menu for switching identity when interacting with this post" id="ember1793" class="artdeco-button artdeco-button--muted artdeco-button--4 artdeco-button--tertiary ember-view align-items-center social-actions-button content-admin-identity-toggle-button"><!---->
<span class="artdeco-button__text">
    
        <div class="content-admin-identity-toggle-button__image-and-caret-wrapper">
            <img src="https://media.licdn.com/dms/image/v2/D4E35AQGpp9o3t9TbVw/profile-framedphoto-shrink_100_100/profile-framedphoto-shrink_100_100/0/1724455776612?e=1727359200&amp;v=beta&amp;t=Jy5folMOCojzWpT-TRK_XET0XnlVlghrs2L_a6_tfyo" loading="lazy" alt="Photo of Pablo Tomas Borda" id="ember1794" class="EntityPhoto-circle-0 evi-image lazy-image ember-view">
          <svg role="none" aria-hidden="true" class="ml1" xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16" data-supported-dps="16x16" data-test-icon="caret-small">
<!---->    
    <use href="#caret-small" width="16" height="16"></use>
</svg>

        </div>
      
</span></button>

<!---->    </div>
  
              
    <span class="reactions-react-button feed-shared-social-action-bar__action-button">
<!---->
      <button aria-pressed="true" aria-label="Unreact Like" id="ember1795" class="artdeco-button artdeco-button--muted artdeco-button--4 artdeco-button--tertiary ember-view social-actions-button react-button__trigger
          react-button--active"><!---->
<span class="artdeco-button__text">
    
        <div class="flex-wrap justify-center
            artdeco-button__text align-items-center">
              
    <img class="reactions-icon artdeco-button__icon reactions-react-button__icon reactions-icon__creation--small data-test-reactions-icon-type-LIKE data-test-reactions-icon-theme-light" src="https://static.licdn.com/aero-v1/sc/h/5zhd32fqi5pxwzsz78iui643e" alt="like" data-test-reactions-icon-type="LIKE" data-test-reactions-icon-theme="light">
  

            <span aria-hidden="true" class="artdeco-button__text react-button__text social-action-button__text
                react-button__text--like">
              Like
            </span>
        </div>
      
</span></button>

      <button aria-label="Open reactions menu" aria-expanded="false" id="ember1796" class="artdeco-button artdeco-button--muted artdeco-button--2 artdeco-button--tertiary ember-view reactions-menu__trigger" data-finite-scroll-hotkey="l"><!---->
<span class="artdeco-button__text">
    
        <svg role="none" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16" data-supported-dps="16x16" data-test-icon="caret-small">
<!---->    
    <use href="#caret-small" width="16" height="16"></use>
</svg>

      
</span></button>
    </span>
  
              <span tabindex="-1" id="ember1797" class="artdeco-hoverable-trigger artdeco-hoverable-trigger--content-placed-top artdeco-hoverable-trigger--is-hoverable ember-view feed-shared-social-action-bar__action-button">
  <div>
    <button role="button" aria-label="Comment" id="feed-shared-social-action-bar-comment-ember1792" class="artdeco-button artdeco-button--muted artdeco-button--4 artdeco-button--tertiary ember-view social-actions-button comment-button flex-wrap " data-finite-scroll-hotkey="c">        <svg role="none" aria-hidden="true" class="artdeco-button__icon " xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" data-supported-dps="24x24" data-test-icon="comment-medium">
<!---->    
    <use href="#comment-medium" width="24" height="24"></use>
</svg>


<span class="artdeco-button__text">
    Comment
</span></button>
  </div>
  <div id="artdeco-gen-96" class="ember-view"><div id="ember1800" class="ember-view"></div></div>
</span>
              
    <div id="ember1801" class="artdeco-dropdown artdeco-dropdown--placement-bottom artdeco-dropdown--justification-right ember-view feed-shared-social-action-bar__action-button">
      <span tabindex="-1" id="ember1803" class="artdeco-hoverable-trigger artdeco-hoverable-trigger--content-placed-top artdeco-hoverable-trigger--is-hoverable ember-view flex-1 display-flex">
        <button aria-expanded="false" aria-label="" id="ember1804" class="artdeco-dropdown__trigger artdeco-dropdown__trigger--placement-bottom ember-view 
            artdeco-button social-actions-button social-reshare-button flex-wrap
            artdeco-button--muted artdeco-button--4 artdeco-button--tertiary" data-finite-scroll-hotkey="r" type="button" tabindex="0">
            <svg role="none" aria-hidden="true" class="artdeco-button__icon" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" data-supported-dps="24x24" data-test-icon="repost-medium">
<!---->    
    <use href="#repost-medium" width="24" height="24"></use>
</svg>

            <span class="artdeco-button__text social-action-button__text">Repost</span>
        
<!----></button>

        <div tabindex="-1" aria-hidden="true" id="ember1805" class="artdeco-dropdown__content artdeco-dropdown--is-dropdown-element artdeco-dropdown__content--justification-right artdeco-dropdown__content--placement-bottom ember-view social-reshare-button__share-dropdown-content"><!----></div>

        <div id="artdeco-gen-97" class="ember-view"><div id="ember1807" class="ember-view"></div></div>
      </span>
        <div>
  
      
<!---->  
  """  # Replace YOUR_HTML_CONTENT_HERE with your actual HTML data

# Parse the HTML using BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Function to extract information about comments and reactions
def extract_comments_and_reactions(soup):
    results = []
    # Find all divs that match the structure of a comment block
    comments = soup.find_all('div', class_='feed-shared-update-v2 feed-shared-update-v2--minimal-padding full-height relative')
    
    for comment in comments:
        # Extract the commenter's name, assuming it might be your name or others
        commenter = comment.find('a', {'class': 'ember-view'}).text.strip()
        
        # Extract the comment text
        comment_text = comment.find('div', {'class': 'update-components-text relative update-components-update-v2__commentary'}).text.strip()
        
        # Extract the number of reactions
        reactions = comment.find('button', {'class': 'social-details-social-counts__reactions-count'}).text.strip()
        
        # Add to results list
        results.append({
            'Commenter': commenter,
            'Comment': comment_text,
            'Reactions': reactions
        })
    
    return results

# Extract comments and reactions
comments_data = extract_comments_and_reactions(soup)

# Display the extracted data
for comment_data in comments_data:
    print(f"Commenter: {comment_data['Commenter']}")
    print(f"Comment: {comment_data['Comment']}")
    print(f"Reactions: {comment_data['Reactions']}")
    print('----------------------------------------')
