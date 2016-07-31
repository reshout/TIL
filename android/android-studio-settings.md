# Android Studio Settings

## Filesystem Case-Sensitivity Mismatch

### Solution

`~/Library/Preferences/AndroidStudio2.1/idea.properties`에 다음 내용을 추가

```
idea.case.sensitive.fs=true
```

### Reference

- https://confluence.jetbrains.com/display/IDEADEV/Filesystem+Case-Sensitivity+Mismatch
- https://www.jetbrains.com/help/idea/2016.2/file-idea-properties.html
