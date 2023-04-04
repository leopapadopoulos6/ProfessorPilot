import { useAuth0 } from "@auth0/auth0-react";
import React from "react";
import { Route, Routes } from "react-router-dom";
import { PageLoader } from "./components/page-loader";
import { AuthenticationGuard } from "./components/auth/authentication-guard";
import { AdminPage } from "./pages/admin-page";
import { CallbackPage } from "./pages/callback-page";
import { HomePage } from "./pages/home-page";
import { NotFoundPage } from "./pages/not-found-page";
import { ProfilePage } from "./pages/profile-page";
import { ProtectedPage } from "./pages/protected-page";
import { PublicPage } from "./pages/public-page";
import { ReviewForm } from "./components/review-form/review-form";
import { CourseReviewsPage } from "./pages/course-reviews";
import { CoursesPage } from "./pages/courses";
import { ReviewsList } from "./components/review-list/reviews-list";

export const App = () => {
  const { isLoading } = useAuth0();

  if (isLoading) {
    return (
      <div className="page-layout">
        <PageLoader />
      </div>
    );
  }

  return (
    <Routes>
      <Route path="/" element={<HomePage />} />
      <Route path="/recent_course_reviews" element={<ReviewsList endpoint={"recent_course_reviews"} />}/>

      <Route path="/courses" element={<ReviewForm />}/>
      <Route path="/submit_course_review" element={<ReviewForm/>} />

      <Route path="/coursesPage" element={<CoursesPage />}/>
      <Route path="/coursesPage/:course_code" element={<CourseReviewsPage />} />
      {/* <Route path="/CourseReviewsPage" element={<CourseReviewsPage />}/> */}
      <Route path="/profile" element={<AuthenticationGuard component={ProfilePage} />}/>
      <Route path="/public" element={<PublicPage />} />
      <Route
        path="/protected"
        element={<AuthenticationGuard component={ProtectedPage} />}
      />
      <Route
        path="/admin"
        element={<AuthenticationGuard component={AdminPage} />}
      />
      <Route path="/callback" element={<CallbackPage />} />
      <Route path="*" element={<NotFoundPage />} />
    </Routes>
  );
};
