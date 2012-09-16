GenInc::Application.routes.draw do
  resources :events do
    resources :attendees
  end

  root to: 'events#index'
end
