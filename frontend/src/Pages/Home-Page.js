import React from "react";
// import { Auth0Features } from "../Components/auth0-features";
import { HeroBanner } from "../Components/hero-banner";
import { PageLayout } from "../Components/page-layout";
import { ReviewForm } from "../Components/review-form";

export const HomePage = () => (
  <PageLayout>
    <HeroBanner />
      <ReviewForm/>
  </PageLayout>
);