rule suspicious_autorun {
    meta:
        description = "Detects suspicious autorun.inf files"
        severity = "high"
    strings:
        $autorun = "autorun.inf"
        $open = "open="
        $shell = "shell\\"
    condition:
        $autorun and ($open or $shell)
}

rule potential_malware {
    meta:
        description = "Detects potential malware patterns"
        severity = "medium"
    strings:
        $exe = ".exe"
        $dll = ".dll"
        $vbs = ".vbs"
        $ps1 = ".ps1"
    condition:
        any of them
}

rule suspicious_script {
    meta:
        description = "Detects suspicious script files"
        severity = "high"
    strings:
        $powershell = "powershell"
        $cmd = "cmd.exe"
        $wscript = "wscript"
    condition:
        any of them
} 