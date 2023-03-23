import { useAuth0 } from "@auth0/auth0-react";
import React from "react";
import { Route, Routes } from "react-router-dom";
import { PageLoader } from "./Components/page-loader";
import { AuthenticationGuard } from "./Components/authentication-guard";
import { AdminPage } from "./Pages/Admin-Page";
import { CallbackPage } from "./Pages/Callback-Page";
import { HomePage } from "./Pages/Home-Page";
import { NotFoundPage } from "./Pages/Not-Found-Page";
import { ProfilePage } from "./Pages/Profile-Page";
import { ProtectedPage } from "./Pages/Protected-Page";
import { PublicPage } from "./Pages/Public-Page";


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
      <Route
        path="/profile"
        element={<AuthenticationGuard component={ProfilePage} />}
      />
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