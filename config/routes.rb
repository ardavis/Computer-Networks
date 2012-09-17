GenInc::Application.routes.draw do
  resources :events do
    resources :attendees
  end

  resources :attendees

  root to: 'events#index'
end
