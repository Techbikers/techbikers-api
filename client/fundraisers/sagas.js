import { takeEvery, call, fork } from "redux-saga/effects";
import { Schema, arrayOf } from "normalizr";

import { callApi } from "techbikers/utils/api";
import * as actions from "techbikers/fundraisers/actions";

export const FundraiserSchema = new Schema("fundraiser");

/**
 * Fetch all fundraisers
 */
export function* fetchActiveFundraisers() {
  return yield call(callApi, "/fundraisers/", {}, arrayOf(FundraiserSchema));
}

export function* createFundraiser({ payload }) {
  const { rideId, userId } = payload;
  const fetchOptions = {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      ride: rideId,
      user: userId
    })
  };
  return yield call(callApi, `/rides/${rideId}/riders/${userId}/fundraiser`, fetchOptions, arrayOf(FundraiserSchema));
}

export default function* root() {
  yield [
    fork(takeEvery, actions.FETCH_ACTIVE_FUNDRAISERS, fetchActiveFundraisers),
    fork(takeEvery, actions.CREATE_FUNDRAISER, createFundraiser)
  ];
}
