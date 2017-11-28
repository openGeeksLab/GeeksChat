package com.geekschat;

import android.support.annotation.NonNull;

import com.facebook.react.ReactPackage;
import java.util.Arrays;
import java.util.List;

import com.facebook.soloader.SoLoader;
import com.reactnativenavigation.NavigationApplication;
import com.lugg.ReactNativeConfig.ReactNativeConfigPackage;

public class MainApplication extends NavigationApplication {

  @Override
  public boolean isDebug() {
    return BuildConfig.DEBUG;
  }

  @NonNull
  @Override
  public List<ReactPackage> createAdditionalReactPackages() {
    return Arrays.<ReactPackage>asList(
      new ReactNativeConfigPackage()
    );
  }

  @Override
  public void onCreate() {
    super.onCreate();
    SoLoader.init(this, /* native exopackage */ false);
  }
}
